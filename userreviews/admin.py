from django.contrib import admin
from .models import Category, Restaurant
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Category)