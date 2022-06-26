from django.shortcuts import render, get_object_or_404, redirect

from order.models import Order, OrderItem
from product.models import ProductModel

from account.models import Customer
from django.contrib import messages

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from order.decorators import allowed_user

from order.forms import CheckoutForm


@allowed_user
def add_to_cart(request, slug):
    customer = Customer.objects.get(user=request.user)
    product = get_object_or_404(ProductModel, slug=slug)
    # order_item = OrderItem.objects.create(item=product)
    order = Order.objects.filter(customer=customer, ordered=False)

    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=product.slug).exists():
            order_item = order.items.get(item__slug=product.slug)
            order_item.quantity += 1
            order_item.save()
        else:
            order_item = OrderItem.objects.create(item=product)
            order.items.add(order_item)
    else:
        order = Order.objects.create(
            customer=customer,
        )
        order_item = OrderItem.objects.create(item=product)
        order.items.add(order_item)

    return redirect("ProductDetail", slug=slug)


def remove_to_cart(request, slug):
    customer = Customer.objects.get(user=request.user)
    product = get_object_or_404(ProductModel, slug=slug)
    order = Order.objects.filter(customer=customer, ordered=False)

    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=product.slug).exists():
            order_item = OrderItem.objects.get(
                item=product
            )
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove()
                order_item.delete()

            messages.info(request, "This item was removed from your cart.")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("ProductList")
    else:
        return redirect("ProductList")

    return redirect("ProductList")


class OrderSummaryView(View, LoginRequiredMixin):

    def get(self, *args, **kwargs):
        from django.core.exceptions import ObjectDoesNotExist
        try:
            customer = Customer.objects.get(user=self.request.user)
            order = Order.objects.get(customer=customer, ordered=False)
            # Order Items te alınabilir
            context = {
                'order': order
            }
            return render(self.request, 'order-summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            "form": form
        }
        return render(self.request, 'checkout-page.html', context)

    def post(self, *args, **kwargs):
        pass