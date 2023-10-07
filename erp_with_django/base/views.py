from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    # it's overriding the above variable room
    # it's the query we are adding
    # variable_that_holds_response = model_name.model_obj_attribute.method(all(), get(), filter(), exclude() ))
    # Models by default have id generated for them so it start with 1
    # we can use filter() method
    # q == what we pass in the url
    # topic__name__contains=q this is what we search in url it is case sensitive
    # topic__name__icontains=q i meens it is not case sensitive
    q = request.GET.get('q') if request.GET.get('q')!= None else ''

    rooms = Room.objects.filter(topic__name__contains=q)

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request, "base/home.html", context)

# Hear we will have access to what ever has been stored in pk
def room(request, pk):
    # Comment 1
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    # request is an object
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render('request', 'base/room_form.html', context)


def deleteRoom(request, pk):
    # We want to know which room we are deleting
    room = Room.objects.get(id=pk)
    # Pst method is for confirm
    if request.method == 'POST':
        room.delete()
        # Sending user back to home page
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

    """
    Comment 1
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    We need specific model so commenting this out
    """

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