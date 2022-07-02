from django.db import models
from  django.core.files import File

from PIL import Image
from io import BytesIO

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

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

    def get_absolute_path(self):
        return f"details/{self.slug}"

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000/static" + self.image.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000/static" + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return "http://127.0.0.1:8000/static" + self.thumbnail.url
            return ""

    def __str__(self):
        return self.title


class CarouselModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)

    def __str__(self):
        return self.title
