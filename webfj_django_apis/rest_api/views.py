# -*- coding: utf-8 -*-

"""
File: view.py
Author: jackdan9
Date: 2018/8/17 16:53
"""
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework.views import APIView
class ClassBasedView(APIView):
    """
    docstring
    """
    def get(self, request):
        """

        :param request:
        :return:
        """
        html = 'I am ClassBasedView get func.'
        return HttpResponse(html)
    def post(self, request):
        """

        :param request:
        :return:
        """
        title = 'I am ClassBasedView post func.'
        param1 = request.POST.get('mychoice')
        html = title + "mychoice is:" + str(param1)
        return HttpResponse(html)
