
from django.urls import path
from product.views import product_list

urlpatterns = [
    path('', product_list, name="ProductList"),

]
