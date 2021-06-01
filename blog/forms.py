from django import forms
from django.forms import fields, models
from .models import Post, Media, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content'}

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = {'title', 'document'}

'''class ContactForm(forms.ModelForm):
    class Meta:
        models = Contact
        fields = '__all__' '''

class Subscribe(forms.Form):
    Email = forms.EmailField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email','body'}