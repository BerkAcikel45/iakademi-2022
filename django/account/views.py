import six
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from account.forms import CreateUserForm
from account.models import Customer
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


# utils gibi bir dosyada tutulabilir
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        customer = Customer.objects.get(user=user)

        # Six kütüphanesini kullanıyoruz
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(customer.is_email_vertificated))


generate_token = TokenGenerator()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    email_body = render_to_string('authenticate/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email="Test",
        to=[user.email]
    )
    # threading yapılabilir

    # main
    # email thread
    # thread ve process farkı

    email.send()




def SingUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, name=user.username)

            send_activation_email(user, request)

            # username = form.cleaned_data["username"]
            username = form.cleaned_data.get("username")
            # message
            # print(f"Welcome {username}")
            messages.info(request, f"Welcome {username}, activate your email")

            return redirect("SignIn")
            # return redirect("ProductList")
    context = {"form": form}
    return render(request, "accounts/sign_up.html", context)


def SingIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            customer = Customer.objects.get(user=user)
            if customer.is_email_vertificated:
                login(request, user)
                messages.info(request, f"Welcome {username}")
                return redirect("ProductList")
            else:
                messages.info(request, f"Activate your mail")
        else:
            messages.info(request, "Username or password is incorrect")
    return render(request, "accounts/signin.html", {})


def Logout(request):
    logout(request)
    return redirect("ProductList")


def SingIn_SingUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("ProductList")
            else:
                messages.info(request, "Username or password is incorrect")

    context = {"form": form}
    return render(request, "accounts/sign_up.html", context)


def activate_user(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
        customer = Customer.objects.get(user=user)

    except Exception as e:
        print(e)
        user = None
        customer = None

    if customer and generate_token.check_token(user, token):
        customer.is_email_vertificated = True
        customer.save()

        messages.add_message(request, messages.SUCCESS,
           'Email verified, you can now login')

        return redirect('SignIn')

    return render(request, 'authenticate/activate-fail.html')