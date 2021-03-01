from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserFormR


def register(response):
    if response.method == "POST":        
        form = UserFormR(response.POST)
        try:
            form.clean()
        except:
            print('errorrrrrrrrrr')
            form.password = form['password1']
            form.save()
        else:      
            if form.is_valid():
                form.password = form.cleaned_data.get('password1')
                form.save()

        return redirect("/usr/login")
    else:
        form = UserFormR()

    return render(response, "register.html", {"form":form})

def login(request):
    
    form = UserFormR()
    return render(request, 'login.html', {'form': form})

def profile(request, pk):
    profile = get_object_or_404(UserFormR, pk=pk)
    return render(request, 'profile.html', {'profile': profile})
