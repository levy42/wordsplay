import logging
from django.core import serializers
from ReMinder.models import User

logger = logging.getLogger(__name__)


def register(user):
    user.save()
    logger.info("new user registrated: " + serializers.serialize("json", user))


def delete(id):
    user = User.objects.get(pk=id)
    user.delete()
    logger.info("new user deleted: " + serializers.serialize("json", user))


def edit(id, user):
    record = User.objects.get(pk=id)
    record.name = user.name
    record.password = user.password
    record.save()
    logger.info("user upated: " + serializers.serialize("json", user))


def get(id):
    logger.info("get user with id =%s" % id)
    logger.debug("get user")
    return User.objects.get(pk=id)
