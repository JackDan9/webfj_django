# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

from django.shortcuts import render_to_response

from models import Table

# Create your views here.
def list_doutu(request):
    doutu_list = Table.objects.order_by('-id')
    # doutu_list = Table.objects.all()
    return render_to_response('doutu/doutu.html', {'doutu_list': doutu_list})

def home(request):
    return render_to_response('index.html')
