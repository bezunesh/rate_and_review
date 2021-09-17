from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='userreviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('item/<int:item_id>', views.item, name='item'),
    path('evaluate/<int:item_id>', views.evaluate, name='evaluate'),
    path('reviews/posted/', views.reviewPosted, name='review_was_posted')
]