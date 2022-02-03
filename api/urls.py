from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCategories),
    path('add/', views.addCategory),
    path('category/<int:category_id>', views.getCategory),
    path('item/<int:item_id>', views.getItem),
    path('items/category/<int:category_id>', views.getItemsByCategory),
    path('item/reviews/<int:item_id>', views.getReviews),
]