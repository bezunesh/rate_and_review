from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from userreviews import views 

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.index, name='index'),
   # path('admin/logout', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('reviews/', include('userreviews.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
