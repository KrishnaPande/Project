from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        field = '__all__'


# ModelFrom is class base represenhfhxc tation of form