from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise("User must have an email adress")
        if not username:
            raise("User must have an name")
        user=self.model(email=self.normalize_email(email),username=username,)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(email=self.normalize_email(email),username=username,password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):
    email=models.EmailField(verbose_name="email",max_length=60,unique=True)
    username=models.CharField(max_length=30,unique=True)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    gender=models.CharField(max_length=1,choices=(("M","MALE"),("F","FEMALE")))
    profession=models.CharField(max_length=1,choices=(("S","STUDENT"),("P","PROFESSIONAL")))
    bio=models.CharField(max_length=200)
    profile_photo=models.ImageField(upload_to='images')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username',]
    objects=MyAccountManager()

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class Post(models.Model):
    author=models.ForeignKey(Account,on_delete=models.CASCADE)
    title=models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    content=models.TextField()

class Like(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account,on_delete=models.CASCADE)
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)

class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account,on_delete=models.CASCADE)
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()

class Tags(models.Model):
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    tag=models.CharField(max_length=15)

# class Post(models.Model):
#     date=models.DateTimeField("date published")
#     content = models.TextField()
#     likes=models.ForeignKey(User,on_delete=models.CASCADE)

# class Comment(models.Model):
#     # id = models.IntegerField(model.Integer, primary_key=True)
#     text = models.Column(models.String(200), nullable=False)
#     date_created = models.DateTimeField("date published")
#     author = models.Column(models.Integer, models.ForeignKey(
#         'user.id', ondelete="CASCADE"), nullable=False)
#     post_id = models.Column(models.Integer, models.ForeignKey(
#         'post.id', ondelete="CASCADE"), nullable=False)


# class Like(models.Model):
#     id = models.Column(models.Integer, primary_key=True)
#     date_created = models.DateTimeField("date published")
#     author = models.Column(models.Integer, models.ForeignKey(
#         'user.id', ondelete="CASCADE"), nullable=False)
#     post_id = models.Column(models.Integer, models.ForeignKey(
#         'post.id', ondelete="CASCADE"), nullable=False)