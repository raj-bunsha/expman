from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('posts', views.posts,name="post"),
    path('posts/<int:id>', views.readpost,name="post"),
    path('posts/likepost/<int:id>', views.add_like,name="likepost"),
    path('posts/comment/<int:id>', views.add_comment,name="comment"),
    path('logout', views.logout,name="logout"),
    path('profile', views.profile,name="profile"),
    path('restrict', views.error1,name="error1"),
    path('about_goals', views.about_goals),
    path('about_us', views.about_us),
    path('about_team', views.about_team),
    path('create_post', views.create_post),
    path('contact', views.contact), 
]