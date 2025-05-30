from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),
    path('generos/', include('generos.urls'), name='generos'),
    path('movies/', include('movies.urls'), name='movies'),
    path('users/', include('users.urls'), name='usuarios'),
    path('series/', include('series.urls'), name='series'),
    path('accounts/', include('django.contrib.auth.urls')),
]
