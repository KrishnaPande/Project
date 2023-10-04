from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # This will create form based on the metadata in class(Room) which is in model.py
        fields = '__all__'