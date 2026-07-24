from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class CustomUser(AbstractUser):
    name=models.CharField(max_length=100, blank=False, null=False)
    age=models.PositiveIntegerField(blank=True, default=18)
    phone_number=models.CharField(max_length=30, blank=False)

class Product(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    price=models.PositiveIntegerField(blank=True, default=0)
    descriptions=models.TextField()
    created_at=models.TimeField(auto_now_add=True)
    created_date=models.DateField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)

    def __str__(self):
        return self.name