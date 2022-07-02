
from django.urls import path
from product.views import product_list, details_product, ProductDetailView, ProductListView

urlpatterns = [

    # path('', product_list, name="ProductList"),
    path('', ProductListView.as_view(), name="ProductList"),

    # path('details/<slug>/', details_product, name="ProductDetail"),
    path('details/<slug>/', ProductDetailView.as_view(), name="ProductDetail"),

]
