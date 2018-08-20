# -*- coding: utf-8 -*-

"""
File: view.py
Author: jackdan9
Date: 2018/8/17 16:53
"""

from django.conf.urls import url, include
from rest_framework import routers
from webfj_django_apis.rest_api import views

urlpatterns = [
    url(r'^debug/', views.ClassBasedView.as_view(), name='debug')
]
