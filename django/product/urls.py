
from django.urls import path
from product.views import product_list, details_product

urlpatterns = [

    path('', product_list, name="ProductList"),
    path('details/<slug>/', details_product, name="ProductDetail"),

]
