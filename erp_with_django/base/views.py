from django.shortcuts import render
from .models import Room
from .forms import RoomForm

# Create your views here.

# Render Rooms

'''
Commenting this out as we need dynamic room by bellow query time 1:23:14
rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developers'},
]
'''

def home(request):
    # it's overriding the above variable room
    # it's the query we are adding
    # variable_that_holds_response = model_name.model_obj_attribute.method(all(), get(), filter(), exclude() ))
    # Models by defauld have id generated for them so it start with 1
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)

# Hear we will have access to what ever has been stored in pk
def room(request, pk):
    '''
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    We need specific model so commenting this out
    '''
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.

    context = {'form': form}
    return render(request, 'base/room_form.html', context)