from django.shortcuts import render, get_object_or_404

from product.models import CarouselModel, ProductModel


def product_list(request):
    products = ProductModel.objects.all()  # SELECT * FROM ProductModel
    carousel = CarouselModel.objects.all()  # SELECT * FROM CarouselModel

    return render(request, "home-page.html", {"products": products,
                                              "carousels": carousel})


def details_product(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    return render(request, "product-page.html", {"product": product})