"""webfj_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from webfj_django_doutu import urls as webfj_django_doutu_usls
from webfj_django_doutu import views
# from django.urls import path
# from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/rest_api/', include('webfj_django_apis.rest_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'doutu/',views.)
    url(r'^doutu/', include('webfj_django_doutu.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^table_list/', include('webfj_django_apis.urls')),
    # url(r'^doutu/', include('webfj_django_doutu.views.list_doutu')),
]
