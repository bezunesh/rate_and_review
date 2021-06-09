from django.shortcuts import render
from .models import Category, Restaurant
# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'userreviews/index.html', {'categories': categories})

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'userreviews/category.html', {'category': category})

def restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    return render(request, 'userreviews/restaurant.html', {'r': restaurant})