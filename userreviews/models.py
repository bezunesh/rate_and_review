from django.db import models
from reviews.models import Review
from django.contrib.contenttypes.fields import GenericRelation

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
    logo = models.ImageField(upload_to='logo', default='default.png')
    reviews = GenericRelation(Review, 'object_pk')

    def __str__(self):
        return self.name
