from email.mime import image
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content= models.TextField(max_length=10000)
    active=models.BooleanField()
    publish_date=models.DateTimeField()
    image=models.ImageField(upload_to='posts/')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.title