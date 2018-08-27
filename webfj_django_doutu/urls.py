# -*- coding: utf-8 -*-
from django.conf.urls import url
# from django.views.generic.simple import *
from django.conf.urls import include

from . import views

app_name = 'webfj_django_doutu'

urlpatterns = [
    # url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    # url(r'^doutu/', include('webfj_django_doutu.views.list_doutu')),
    # url(r'^$', views.index, name="index"),
    url(r'^register/', views.register, name="register")
    # url(r'^home/', views.home, name="home"),
]