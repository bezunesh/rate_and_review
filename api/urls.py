from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCategories),
    path('add/', views.addCategory)
]