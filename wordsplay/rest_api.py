import json
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import wordsplay.api.users.users_manager as um
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# user managing

@csrf_exempt
def login(request):
    user = authenticate(username=request.GET["user_name"], password=request.GET["pass"])


@login_required
def get_users(request):
    if request.user.is_authenticated():
        print("access")
    else:
        print("no access")
    users = um.get_all()
    return HttpResponse(serializers.serialize('json', users))


@csrf_exempt
def register_user(request):
    user = User.objects.create_user(request.GET["user_name"], '',
                                    request.GET["pass"])
    um.register(user)
    return HttpResponse("ok")


@login_required
def get_user(request, id):
    user = um.get(id)
    return HttpResponse(serializers.serialize("json", [user]))


@login_required
def delete_user(request, id):
    um.delete(id)
    return HttpResponse("ok")

