from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    def __init__(self, user1, user2, started_at, status):
        self.user1 = user1
        self.user2 = user2
        self.started_at = started_at
        self.log = ""
        self.status =  status
        
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')
    log = models.TextField()
    winner = models.ForeignKey(User, related_name='winner')
    started_at = models.DateTimeField()
    status = models.CharField(max_length=128)
