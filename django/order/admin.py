from django.contrib import admin

from order.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)