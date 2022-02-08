from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import RegisterForm
# Create your views here.
def home(request):
    return render(request,"home.html",{})

def posts(request):
    return render(request,"posts.html",{})

def saved(request):
    return render(request,"saved.html",{})

def signup(request):
    if request.method=="POST":
        form=RegisterForm(request.post)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password')
            account=authenticate(email='email',password='password')
            login(request,account)
            return redirect('home')
    return render(request,"signup.html",{})

def login(request):
    return render(request,"login.html",{})

def your_posts(request):
    return render(request,"your_posts.html",{})

def profile(request):
    return render(request,"profile.html",{})

def contact(request):
    return render(request,"contact.html",{})

def about(request):
    return render(request,"about.html",{})