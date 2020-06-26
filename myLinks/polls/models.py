from django.db import models
from django import forms
# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=250,unique=True)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    password = models.CharField(max_length=50,default="")
    email = models.EmailField()
    description = models.TextField(default="")

    def __str__(self):
        return self.nickname

class Link(models.Model):
    name = models.CharField(max_length=250)
    click_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    color_code = models.CharField(max_length=50,default="#ffffff")
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name