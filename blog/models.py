from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Media(models.Model):
    title = models.CharField(max_length=100, null=True)
    document = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)