from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('posts', views.posts),
    path('signup', views.signup),
    path('login', views.login),
    path('saved', views.saved),
    path('profile', views.profile),
    path('contact', views.contact),
    path('about_goals', views.about_goals),
    path('about_us', views.about_us),
    path('about_team', views.about_team),
    path('create_post', views.create_post),
]