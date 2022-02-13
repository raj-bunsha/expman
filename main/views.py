from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from main.forms import RegisterForm
from .models import *
from django.db.models import Count
from django.contrib.auth.decorators import *
from django.views.decorators.csrf import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    trending=Post.objects.annotate(num_likes=Count("likes")).order_by("-num_likes")[:2]
    print(trending)
    if request.POST and 'signup' in request.POST and not request.user.is_authenticated:
        a,b=signup(request)
        errors=[]
        for field in b:
            for error in field.errors:
                errors.append(error)
        if not a:
            return render(request,"home.html",{"error":"<br>".join(errors),"show":True,"trending":trending})
        else:
            return redirect("profile")

    if request.POST and 'login' in request.POST and not request.user.is_authenticated:
        a,b=login(request)
        if not a:
            return render(request,"home.html",{"error":b,"show":True,"trending":trending})
        else:
            return render(request,"home.html",{"success":" ","show":True,"trending":trending})
    return render(request,"home.html",{"trending":trending})

def posts(request):
    show=""
    if request.method=="GET" and 'searchb' in request.GET:
        using,search=request.GET.get('using'),request.GET.get('search')
        show=search
        if request.user:
            Search_history(search=search,user=request.user.username).save()
        else:
            Search_history(search=search,user="Anonymus").save()
        if using=="Tags":
            posts=[]
            for i in Tags.objects.filter(tag__contains=search):
                posts.append(i.Post)
        if using=="Text":
            posts=Post.objects.filter(content__contains=search)
    else:
        posts=Post.objects.all()[::-1]
    return render(request,"posts.html",{"posts":posts,"show":show})

def signup(request):
    form=RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        email=form.cleaned_data.get('email')
        raw_password=form.cleaned_data.get('password1')
        account=authenticate(email=email,password=raw_password)
        auth_login(request,account)
        return True,{}
    else:
        return False,form
    

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
    if request.POST:
        gender=request.POST.get("genradio")
        cat=request.POST.get("cat")
        if gender=="male":
            gender="M"
        else:
            gender="F"
        if cat=="prof.":
            cat="P"
        else:
            cat="S"
        t=Account.objects.get(id=request.user.id)
        t.gender=gender
        t.profession=cat
        t.bio=request.POST.get('bio')
        t.save()
        return HttpResponseRedirect("/")
    return render(request,"profile.html",{})

def contact(request):
    return render(request,"contact.html",{})

def about_us(request):
    return render(request,"about_us.html",{})

def about_team(request):
    return render(request,"about_team.html",{})

def about_goals(request):
    return render(request,"about_goals.html",{})

def readpost(request,id):
    post=Post.objects.get(id=id)
    return render(request,"readpost.html",{"post":post,"user_likes":post.likes.all(),"likes":post.number_of_likes(),"comments":post.comment_set.all()})

@login_required
def create_post(request):
    if request.POST:
        data=request.POST
        print(data)
        t=Post(author=request.user,title=data.get('title'),content=data.get('content'))
        a,b,c=Tags(Post=t,tag=data.get('tag1')),Tags(Post=t,tag=data.get('tag2')),Tags(Post=t,tag=data.get('tag3'))
        t.save()
        a.save()
        b.save()
        c.save()
    return render(request,"create_post.html",{})

def error1(request):
    return render(request,"error.html",{})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def add_like(request,id):
    print(request.POST)
    post = get_object_or_404(Post, id=request.POST.get('like'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post', args=[str(id)]))

@login_required
def add_comment(request,id):
    post = get_object_or_404(Post, id=id)
    comment=Comment(author=request.user,Post=post,comment=request.POST['comment'])
    comment.save()
    return HttpResponseRedirect(reverse('post', args=[str(id)]))