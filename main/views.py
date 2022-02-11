from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from flask_login import login_required
from .forms import RegisterForm
from .models import *
# Create your views here.
def home(request):
    if request.POST and 'signup' in request.POST:
        a,b=signup(request)
        print(b)
        if not a:
            return render(request,"home.html",{"error":b,"show":True})
        else:
            return render(request,"home.html",{"success":" ","show":True})
    if request.POST and 'login' in request.POST:
        a,b=login(request)
        print(a)
        if not a:
            return render(request,"home.html",{"error":b,"show":True})
        else:
            return render(request,"home.html",{"success":" ","show":True})
    return render(request,"home.html",{})

def posts(request):
    posts=Post.objects.all()
    return render(request,"posts.html",{"posts":posts})

def saved(request):
    return render(request,"saved.html",{})

def signup(request):
    context={}
    
    form=RegisterForm({"username":request.POST["username"],"email":request.POST["email"],"password1":request.POST["password1"],"password2":request.POST["password2"]})
    if form.is_valid():
        form.save()
        email=form.cleaned_data.get('email')
        raw_password=form.cleaned_data.get('password1')
        account=authenticate(email=email,password=raw_password)
        auth_login(request,account)
        return True,{}
    else:
        return False,form.errors
    

def login(request):
    account=authenticate(email=request.POST.get('email'),password=request.POST.get("password"))
    if account:
        auth_login(request,account)
        return True,""
    else:
        return False,"Invalid Email Address/Password"

def your_posts(request):
    return render(request,"your_posts.html",{})

def profile(request):
    return render(request,"profile.html",{})

def contact(request):
    return render(request,"contact.html",{})

def about_us(request):
    return render(request,"about_us.html",{})

def about_team(request):
    return render(request,"about_team.html",{})

def about_goals(request):
    return render(request,"about_goals.html",{})

def create_post(request):
    if request.POST:
        data=request.POST
        t=Post(author=request.user,title=data.get('title'),content=data.get('content'))
        a,b,c=Tags(Post=t,tag=data.get('tag1')),Tags(Post=t,tag=data.get('tag2')),Tags(Post=t,tag=data.get('tag3'))
        t.save()
        a.save()
        b.save()
        c.save()
    return render(request,"create_post.html",{})

def logout(request):
    auth_logout(request)
    return redirect('home')