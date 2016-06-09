"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from wordsplay.views import home
from registration import auth_urls
from registration.backends.model_activation import urls as registration_urls
from wordsplay.views import test

import wordsplay.rest_api as rest

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='index'),
    url(r'^auth/', include(auth_urls)),
    url(r'^auth/', include(registration_urls)),
    url(r'^test/', test)
]
