import json
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from wordsplay.game import game_manager as gm


def create_game_request(request):
    return HttpResponse(
        gm.create_game_request(request.user, request.GET.get('time')))


def cencel_game_request(request):
    return HttpResponse(gm.cencel_game_request(request.user))


def get_game_requests(request):
    return HttpResponse(str(gm.get_game_requests(request.user)))


def apply_request(request):
    return HttpResponse(gm.apply_request(request.GET.get('id'), request.user))
