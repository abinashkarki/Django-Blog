from blog.models import Comment, Media, Post
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(Comment)
