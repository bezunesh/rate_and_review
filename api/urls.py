from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiList, name="List all api endpoints"),
    path('categories/', views.CategoryList.as_view(), name="List all categories"),
    path('add/category/', views.CategoryList.as_view(), name="Add a new category"),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name="Get a category by id"),
    path('item/<int:pk>', views.ItemDetail().as_view(), name="Get an item by id"),
    path('items/category/<int:category_id>', views.ItemList.as_view(), name="Get all items of a category"),
    path('item/reviews/<int:pk>', views.ItemReviews.as_view(), name="Get all reviews of an item"),
]