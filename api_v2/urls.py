from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.listCategories),
    path('add/category/', views.addCategory)
]