from django.shortcuts import render, get_object_or_404, redirect

from order.models import Order, OrderItem
from product.models import ProductModel

from account.models import Customer


def add_to_cart(request, slug):
    customer = Customer.objects.get(user=request.user)
    product = get_object_or_404(ProductModel, slug=slug)
    order_item = OrderItem.objects.create(item=product)
    order = Order.objects.filter(customer=customer, ordered=False)

    if order.exists():
        order = order[0]

        if order.items.filter(item__slug=product.slug).exists():
            order_item.quantity += 1
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(
            customer=customer
        )
        order.items.add(order_item)

    return redirect("ProductDetail", slug=slug)