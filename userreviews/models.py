from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name) if self.name else ''

class Item(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) if self.name else ''

class User(AbstractUser):
    email = models.EmailField('email address', blank=False)
    
    class Meta:
        db_table = 'auth_user'
