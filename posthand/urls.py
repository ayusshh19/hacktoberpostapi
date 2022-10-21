from django.contrib import admin
from django.urls import path

from .views import add_post, home

urlpatterns = [
    path('getpost/',home,name='home_of_api'),
    path('addpost/',add_post,name='add_post')
]
