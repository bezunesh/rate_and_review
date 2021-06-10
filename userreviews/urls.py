from django.urls import path
from . import views

app_name='userreviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('item/<int:item_id>', views.item, name='item'),
    path('evaluate/<int:item_id>', views.evaluate, name='evaluate'),
    #path(r'^reviews/', include('reviews.urls')),
]