from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Category, Item
from .forms import SignupForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'userreviews/index.html', {'categories': categories})

def category(request, category_id):
    get_object_or_404(Category, pk=category_id)

    items = Item.objects.filter(category_id=category_id)
    return render(request, 'userreviews/category.html', {'items': items})

def item(request, item_id):
    obj = get_object_or_404(Item, pk=item_id)
    
    return render(request, 'userreviews/item.html', {'item': obj})

def evaluate(request, item_id):
    obj = get_object_or_404(Item, pk=item_id)
    return render(request, 'userreviews/evaluate.html', {'item': obj})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #firstName = form.cleaned_data['first_name']
            #lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            User.objects.create_user(username, email=email, password=password)
            messages.add_message(request, messages.INFO, "User account created successfully!")
            return HttpResponseRedirect(reverse('userreviews:login'))
    else:
        form = SignupForm()
    return render(request, 'registration/sign_up.html', {'form': form})   
