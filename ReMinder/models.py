from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    create_date = models.DateTimeField()
    dest_date = models.DateTimeField()
    text = models.TextField()
