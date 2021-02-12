from django.contrib import admin
from .models import Post

# Create new admin user: python manage.py createsuperuser
 
# Register your models here.
admin.site.register(Post)