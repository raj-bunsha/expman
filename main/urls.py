from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('posts', views.posts),
    path('signup', views.signup),
    path('login', views.login),
    path('saved', views.saved),
    path('', views.home),
    path('', views.home),
]