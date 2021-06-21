from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='userreviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('item/<int:item_id>', views.item, name='item'),
    path('evaluate/<int:item_id>', views.evaluate, name='evaluate'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
    #path(r'^reviews/', include('reviews.urls')),
]