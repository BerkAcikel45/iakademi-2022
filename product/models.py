from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()


class ProductModel(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="uploads/product", blank=True, null=True)
    description = models.TextField(max_length=1000)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_new = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to="uploads/product", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-date_added", )


    def __str__(self):
        return self.title

