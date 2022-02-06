from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('posts', views.posts),
    path('signup', views.signup),
    path('login', views.login),
    path('saved', views.saved),
    path('my_posts', views.your_posts),
    path('profile', views.profile),
    path('contact', views.contact),
]