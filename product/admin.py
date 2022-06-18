from django.contrib import admin

from product.models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductModel, ProductAdmin )
