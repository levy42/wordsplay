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
from wordsplay.views import home
from registration import auth_urls
from registration.backends.simple import urls as registration
from wordsplay.views import *
from wordsplay.rest_api import *

import wordsplay.rest_api as rest

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    # auth and registration
    url(r'^auth/', include(auth_urls)),
    url(r'^auth/', include(registration)),
    # user profiles
    url(r'^profile/', user_profile, name='profile'),
    # games
    url(r'^game/requests/', get_game_requests),
    url(r'^game/apply/(?P<id>[0-9]{4})', apply_request),
    url(r'^game/create/', create_game_request),
    url(r'^game/ring/', games_requests),
]
