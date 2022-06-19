from django.contrib import admin

from product.models import Category, CarouselModel, ProductModel


class ProductAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class CarouselModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CarouselModel, CarouselModelAdmin)
