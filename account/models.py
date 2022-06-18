from django.contrib.auth.models import User
from django.db import models



# CREATE TABLE customer (user_id, varchar name,varchar last_name,. )
#
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(null=True)


