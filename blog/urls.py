from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name="post_new"),
    path('file_upload/', views.upload, name = 'upload'),
    path('send_email/', views.subscribe, name='send_mail')
]