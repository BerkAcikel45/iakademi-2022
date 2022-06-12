
from django.urls import path
from account.views import SingUp, SingIn, Logout

urlpatterns = [
    path('signup/', SingUp, name="SignUp"),
    path('signin/', SingIn, name="SignIn"),
    path('logout/', Logout, name="Logout")

]
