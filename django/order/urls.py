
from django.urls import path
from order.views import add_to_cart

urlpatterns = [

    path('add_to_cart/<slug>/', add_to_cart, name="add_to_cart"),

]
