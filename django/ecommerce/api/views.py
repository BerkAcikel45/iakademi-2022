from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from order.models import Order


# Serializers define the API representation.
class OrderSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_name(self, order):
        return order.customer.name



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer,
