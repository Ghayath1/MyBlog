from email.policy import default
from time import timezone
from django.db import models
from django.utils import timezone
from posts.models import Post
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    create_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.comment