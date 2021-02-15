from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
