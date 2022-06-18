from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from account.forms import CreateUserForm


def SingUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            # username = form.cleaned_data["username"]
            username = form.cleaned_data.get("username")
            # message
            # print(f"Welcome {username}")
            messages.info(request, f"Welcome {username}")
            # return redirect("ProductList")
    context = {"form": form}
    return render(request, "accounts/sign_up.html", context)


def SingIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"Welcome {username}")
            return redirect("ProductList")
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
