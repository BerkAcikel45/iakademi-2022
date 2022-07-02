
from django.urls import path
from api.views import UserViewSet

urlpatterns = [

    path('order/', UserViewSet.as_view({'get': 'list'}), name="order_api"),

]
