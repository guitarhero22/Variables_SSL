from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path('', views.home, name="home"),
    path("logout", views.logout, name='logout'),
    path('helios', views.helios, name='helios'),
    path('profile', views.profile, name='profile'),
    path('change_password', views.change_password, name='change_password')
]
