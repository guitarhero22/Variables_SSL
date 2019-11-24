from django.urls import path
from . import views

urlpatterns = [
 path('', views.build , name = 'build')
]
