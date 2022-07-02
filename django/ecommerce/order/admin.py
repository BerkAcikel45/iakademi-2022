from django.contrib import admin

from order.models import Order, OrderItem, Payment


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)