# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TableManager(models.Manager):
    def query_by_id(self):
        query = self.get_queryset().order_by('-id')
        return query

@python_2_unicode_compatible
class NewUser(AbstractUser):
    profile = models.CharField('profile', default='', max_length=256)
    gender = models.CharField(max_length=5, choices=(('man', '男'), ('woman', '女')))

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username

@python_2_unicode_compatible
class Table(models.Model):
    objects = TableManager()
    title = models.CharField(max_length=50)
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'table'
        verbose_name_plural = 'table'

class Poll(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    table = models.ForeignKey('Table', null=True)
