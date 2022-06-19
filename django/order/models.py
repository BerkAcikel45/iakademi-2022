from django.db import models

from account.models import Customer
from product.models import ProductModel


class OrderItem(models.Model):
    item = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    Status = (
        ("Pending", "Pending"),
        ("Out of Delivery", "Out of Delivery"),
        ("Delivered", "Delivered")
    )
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(OrderItem)
    dateCrated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=Status)
    note = models.CharField(max_length=200, null=True, blank=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name

