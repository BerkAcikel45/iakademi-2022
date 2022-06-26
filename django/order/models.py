from django.db import models

from account.models import Customer
from product.models import ProductModel


class OrderItem(models.Model):
    item = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)


    def get_total_price(self):
        return self.quantity * self.item.price


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

    def get_total_price(self):
        total = 0
        for order_items in self.items.all():
            total += order_items.get_total_price()
        return total

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=True)