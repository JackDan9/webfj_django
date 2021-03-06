# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import Table, Poll, NewUser
from webfj_django.forms import LoginForm, RegisterForm, SetInfoForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

import urlparse

def login(request):
    return render(request, '/')

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/users/login')
    else:
        form = RegisterForm()
    return render(request, 'doutu/register.html', context={'form': form, 'next': redirect_to})

def index(request):
    """

    :param request:
    :return:
    """
    # doutu_list = Table.objects.query_by_id()
    # loginform = LoginForm()
    # context = {'doutu_list': doutu_list, 'loginform': loginform}
    # return render(request, 'index.html', context)
    return render(request, 'index.html')

# from models import NewUser

# Create your views here.
# def list_doutu(request):
    # doutu_list = Table.objects.order_by('-id')
    # doutu_list = Table.objects.all()
    # return render_to_response('doutu/doutu.html', {'doutu_list': doutu_list})

# def home(request):
    # return render_to_response('index.html')
