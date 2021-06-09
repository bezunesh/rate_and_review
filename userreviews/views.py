from django.shortcuts import render
from .models import Restaurant
# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'userreviews/index.html', {'restaurants': restaurants})

def restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    return render(request, 'userreviews/restaurant.html', {'r': restaurant})