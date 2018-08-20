# -*- coding: utf-8 -*-

"""
File: serializers.py
Author: jackdan9
Date: 2018/8/18 12:14
"""

from rest_framework import serializers
from webfj_django_doutu.models import Table

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length = 50)
    img_url = serializers.CharField(required=True, allow_blank=False, max_length = 255)

    def create(self, validated_data):
        """
        Create and return a new `Table` instance, given the validated_data
        :param validated_data:
        :return:
        """
        return Table.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        :param instance:
        :param validated_data:
        :return:
        Update and return an existing `Table` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.img_url = validated_data.get('img_url', instance.img_url)
        instance.save()
        return instance

