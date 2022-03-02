from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories),
    path('category/<int:pk>', views.categories),
    path('items/', views.items),
    path('item/<int:pk>', views.items),
    path('reviews/item/<int:pk>', views.reviews)
]