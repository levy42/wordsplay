import json
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import ReMinder.api.users.users_manager as um
from ReMinder.models import User


# user managing
@csrf_exempt
def register_user(request):
    user = User(name=request.GET["user_name"], password=request.GET["pass"])
    um.register(user)
    return HttpResponse("ok")


@csrf_exempt
def get_user(request, id):
    user = um.get(id)
    return HttpResponse(json.dumps({"name": user.name, "pass": user.password}))

@csrf_exempt
def delete_user(request, id):
    um.delete(id)
    return HttpResponse("ok")

# note managing


