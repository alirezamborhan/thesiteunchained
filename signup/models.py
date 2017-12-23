from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)
    date_registered = models.CharField(max_length=100)
    def __str__(self):
        return self.username
