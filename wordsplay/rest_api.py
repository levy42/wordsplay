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
    game_requests = gm.get_game_requests(request.user)
    result = map(
        lambda r: dict(id=r.user.id, username=r.user.username,
                       time=r.move_time),
        game_requests.values())
    return HttpResponse(str(result))


def apply_request(request):
    return HttpResponse(gm.apply_request(request.GET.get('id'), request.user))
