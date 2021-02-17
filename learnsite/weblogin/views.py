from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def profile(request, pk):
    profile = get_object_or_404(SignUpForm, pk=pk)
    return render(request, 'profile.html', {'profile': profile})



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    
    form = SignUpForm()
    return render(request, 'login.html', {'form': form})

