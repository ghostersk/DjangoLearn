from django.db import models


class UserReg(models.Model):
    username = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.EmailField(max_length=244)
    password = models.CharField(max_length=244)
    birth_date = models.DateField()

    def __str__(self):
        return self.username
