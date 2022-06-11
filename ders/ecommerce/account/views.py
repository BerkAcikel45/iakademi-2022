from django.shortcuts import render

from account.forms import CreateUserForm


def SingUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            # message
            print(f"Welcome {username}")
    context = {"form": form}
    return render(request, "accounts/sign_up.html", context)
