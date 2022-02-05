from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('add/category/', views.CategoryList.as_view()),
    path('category/<int:category_id>', views.CategoryDetail.as_view()),
    path('item/<int:item_id>', views.ItemDetail().as_view()),
    path('items/category/<int:category_id>', views.ItemList.as_view()),
    path('item/reviews/<int:item_id>', views.ItemReviews.as_view()),
]