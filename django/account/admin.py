from django.contrib import admin

from account.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin )
