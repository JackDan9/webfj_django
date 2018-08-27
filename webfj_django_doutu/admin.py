# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django import forms
from .models import Table, NewUser

# Register your models here.
# @admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_url')
    
# @admin.register
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'profile')

admin.site.register(Table, TableAdmin)
admin.site.register(NewUser, NewUserAdmin)
