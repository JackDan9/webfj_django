# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webfj_django_apis.models import Table
from webfj_django_apis.serializers import TableSerializer

@csrf_exempt
def table_list(request):
    """
    List all code table, or create a new table
    :param request:
    :return:
    """
    if request.method == 'GET':
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return JSONParser(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TableSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def table_detail(request, pk):
    """
    Retrieve, update or delete a code table
    :param request:
    :param pk:
    :return:
    """
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(table)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TableSerializer(table, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        table.delete()
        return HttpResponse(status=204)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")





# Create your views here.
