from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiList, name="List all api endpoints"),
    path('categories/', views.CategoryList.as_view(), name="List all categories or create a category"),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name="Retrieve a category by id, update or delete"),
    path('item/<int:pk>', views.ItemDetail().as_view(), name="Retreive an item by id, update or delete"),
    path('items/category/<int:category_id>', views.ItemList.as_view(), name="List all items of a single category or create an item for a category"),
    path('item/reviews/<int:pk>', views.ItemReviews.as_view(), name="List all reviews of an item"),
    path('', include('rest_framework.urls'))
]