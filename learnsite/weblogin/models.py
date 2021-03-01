from django.db import models


class UserReg(models.Model):
    username = models.CharField(max_length=50, help_text = "Username is used to log on to website")
    alias = models.CharField(max_length=50, help_text = "Others will know you under this name, cannot be same as username")
    email = models.EmailField(max_length=244, help_text = "Email address is only for account management")
    password = models.CharField(max_length=244)
    birth_date = models.DateField()

    def __str__(self):
        return self.username
