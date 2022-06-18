
from django.urls import path
from account.views import SingUp, SingIn, SingIn_SingUp, Logout

urlpatterns = [
    path('signup/', SingUp, name="SignUp"),
    path('signin/', SingIn, name="SignIn"),
    path('logout/', Logout, name="Logout"),

    path('signinsignout/', SingIn_SingUp, name="SignIn"),

]
