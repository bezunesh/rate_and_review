from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('add/category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('item/<int:pk>', views.ItemDetail().as_view()),
    path('items/category/<int:category_id>', views.ItemList.as_view()),
    path('item/reviews/<int:pk>', views.ItemReviews.as_view()),
]