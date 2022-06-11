
from django.urls import path
from account.views import SingUp

urlpatterns = [
    path('signup/', SingUp, name="SingUp")
]
