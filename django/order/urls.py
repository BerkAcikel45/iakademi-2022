
from django.urls import path
from order.views import add_to_cart, remove_to_cart, OrderSummaryView, CheckoutView

urlpatterns = [

    path('add_to_cart/<slug>/', add_to_cart, name="add_to_cart"),
    path('remove_to_cart/<slug>/', remove_to_cart, name="remove_to_cart"),

    path('summary', OrderSummaryView.as_view(), name="summary"),

    path('checkout', CheckoutView.as_view(), name="checkout"),

]
