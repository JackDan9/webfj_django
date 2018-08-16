# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Table(models.Model):
    title = models.CharField(max_length=50)
    img_url = models.CharField(max_length=255)