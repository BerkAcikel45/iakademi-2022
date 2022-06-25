from django import template
from order.models import Order
from account.models import Customer

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        customer = Customer.objects.get(user=user)
        qs = Order.objects.filter(customer=customer, ordered=False)

        if qs.exists():
            return qs[0].items.count()

        return 0

