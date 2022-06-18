from django.shortcuts import render

from product.models import ProductModel

def product_list(request):
    products = ProductModel.objects.all()  # SELECT * FROM ProductModel
    return render(request, "home-page.html", {"products": products})
