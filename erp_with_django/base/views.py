from django.shortcuts import render

# Create your views here.

# Render Rooms

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developers'},
]
def home(request):
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)

# Hear we will have access to what ever has been stored in pk
def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    context = {'form: form'}
    return render(request, 'base/room_form.html', context)