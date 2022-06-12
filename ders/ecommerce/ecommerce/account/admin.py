from django.contrib import admin

from account.models import Customer

class a(admin.ModelAdmin):
    pass

admin.site.register(Customer,a )
