from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from userreviews import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.home, name='home'),
   # path('admin/logout', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('reviews/', include('userreviews.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('', include('rest_framework.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


