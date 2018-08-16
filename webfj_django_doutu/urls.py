# -*- coding: utf-8 -*-
from django.conf.urls import url
# from django.views.generic.simple import *
from django.conf.urls import include

from . import views

urlpatterns = [
    # url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    # url(r'^doutu/', include('webfj_django_doutu.views.list_doutu')),
    url(r'^$', views.list_doutu, name="list_doutu"),
    url(r'^home/', views.home, name="home"),
]