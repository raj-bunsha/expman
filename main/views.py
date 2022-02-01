from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def posts(request):
    return render(request,"posts.html",{})

def saved(request):
    return render(request,"saved.html",{})

def signup(request):
    return render(request,"signup.html",{})

def login(request):
    return render(request,"login.html",{})