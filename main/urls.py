from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('posts', views.posts,name="post"),
    path('posts/<int:id>', views.readpost,name="post"),
    path('logout', views.logout,name="logout"),
    path('profile', views.profile),
        
    path('about_goals', views.about_goals),
    path('about_us', views.about_us),
    path('about_team', views.about_team),
    path('create_post', views.create_post),
    path('contact', views.contact), 
]