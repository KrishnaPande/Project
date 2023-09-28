from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

class Topic(models.Model):
    # Hear we are assigning what is topics name(All topic will have name)
    # Topic can have multiple rooms but room will have only one topic
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    # host =
    # As we are setting SET_NULL we need to allow null values in db
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    # when ever save is clicked it will go and add a time stamp
    updated = models.DateTimeField(auto_now=True)
    # auto_now will save at every single time and auto_now_add will save only fist instance
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Massage(models.Model):
    # One-to-many relationship user can have many msg
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when room is deleted we need children also be deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name