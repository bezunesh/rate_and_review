from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Category, Item
#from .forms import SignupForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'userreviews/index.html', {'categories': categories})

def category(request, category_id):
    get_object_or_404(Category, pk=category_id)

    items = Item.objects.filter(category_id=category_id)
    return render(request, 'userreviews/category.html', {'items': items})

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    return render(request, 'userreviews/item.html', {'item': item})

def evaluate(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'userreviews/evaluate.html', {'item': item}) 
