from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.logIn, name="login"),
    path('singin/', views.singIn, name="singin"),
    path('logout/', views.logOut, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
]