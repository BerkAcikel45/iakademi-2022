from django.shortcuts import render, get_object_or_404

from product.models import CarouselModel, ProductModel

from django.views.generic import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin


def product_list(request):
    products = ProductModel.objects.all()  # SELECT * FROM ProductModel
    carousel = CarouselModel.objects.all()  # SELECT * FROM CarouselModel

    return render(request, "home-page.html", {"products": products,
                                              "carousels": carousel})


def details_product(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    return render(request, "product-page.html", {"product": product})


class ProductListView(ListView):
    model = ProductModel
    template_name = "home-page.html"
    paginate_by = 1


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = ProductModel
    template_name = "product-page.html"