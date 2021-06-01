from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import MediaForm, PostForm, Subscribe, CommentForm
from django.core.paginator import Page, PageNotAnInteger, Paginator
# Create your views here.

def about(request):
      posts = Post.objects.all()
      paginator = Paginator(posts, 3)
      page = request.GET.get('page')
      try:
        posts = paginator.page(page)
      except PageNotAnInteger:
        posts = paginator.page(1)

      return render (request, 'blog/about.html', {'page':page, 'posts':posts})

def home(request):
    return render(request, 'blog/home.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active = True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            #assign current post to comment
            new_comment.post = post
            new_comment.save() 
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments':comments, 'new_comment':new_comment, 'commment_form':comment_form})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('about') 
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form':form})


def upload(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        form.save()
        return redirect('about')
    else:
        form = MediaForm()
    return render(request, 'blog/file_upload.html', {'form':form})


from achievers_project.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to My first automated mail sending'
        message = 'You are viewing this mail from my django mail sendng functionality'
        recepient = str(sub['Email'].value())

        print(recepient)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'blog/success.html', {'recepient': recepient})
    return render(request, 'blog/subscribe.html', {'form':sub})