from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')
    log = models.TextField()
    winner = models.ForeignKey(User, related_name='winner')
    started_at = models.DateTimeField()
    status = models.CharField(max_length=128)
