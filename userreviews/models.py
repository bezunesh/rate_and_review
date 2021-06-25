from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

