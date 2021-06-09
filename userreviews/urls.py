from django.urls import path
from . import views

app_name='userreviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/<int:restaurant_id>', views.restaurant, name='restaurant'),
    path('category/<int:category_id>', views.category, name='category'),
    #path(r'^reviews/', include('reviews.urls')),
]