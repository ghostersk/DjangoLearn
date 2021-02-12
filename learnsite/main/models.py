from django.conf import settings
from django.db import models
from django.utils import timezone

# https://tutorial.djangogirls.org/en/django_models/
# Create your models here. class Name(midels.Model):
# Submit models.py change: python manage.py makemigrations <name of app>
# Apply models.py change: manage.py migrate <name of app>

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
