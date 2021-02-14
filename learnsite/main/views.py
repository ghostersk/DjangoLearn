from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import RegUser, LogUser
from django.utils import timezone

# https://tutorial.djangogirls.org/en/django_models/
def index(request):

    return render(request, 'index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def register(request):
    
    if request.method == "POST":
        form = RegUser()
        if form.is_valid():
            usr = form.save(commit=False)
            # Other things can go here, before form is saved
            # usr.author = request.user
            # usr.published_date = timezone.now()
            usr.save()
    else:
        form = RegUser()
    return render(request, 'account/register.html', {'form': form})

def login(request):
    
    if request.method == "POST":
        form = LogUser()
        if form.is_valid():
            usr = form.__getitem__('username')
            paswrd = form.__getitem__('password')
            
            # Other things can go here, before form is saved
            # usr.author = request.user
            # usr.published_date = timezone.now()
            usr.save()
    else:
        form = LogUser()
    return render(request, 'account/register.html', {'form': form})
