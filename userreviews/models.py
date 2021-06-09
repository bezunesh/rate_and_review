from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
