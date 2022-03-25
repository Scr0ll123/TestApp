from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):

    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    autor = models.ForeignKey('Autors',on_delete=models.PROTECT,null=True)
    user = models.ForeignKey(User,verbose_name='Пользователь',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Autors(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30,default='-')
    date_birth = models.DateField()

    def __str__(self):
        return self.name
