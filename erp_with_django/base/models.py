from django.db import models
from django.contrib.auth import User
# Create your models here.

class Room(models.Model):
    # host =
    # topic =
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
    # user =
    # when room is deleted we need children also be deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name