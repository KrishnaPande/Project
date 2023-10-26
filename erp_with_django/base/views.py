from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RoomForm
from .models import Room, Topic, Message


def loginPage(request):
    # we get username and passs

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # if user exist
        try:
            user = User.objects.get(username=username)
        # if not exist
        except:
            messages.error(request, 'user does not exist')

        # if exist authenticate it
        user = authenticate(request, username=username, password=password)

        # use login build in function if yes and redirect the user to home page
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')


    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    # we pass in the user data
    if request.method == 'POST':
        # we push that into user creation form
        form = UserCreationForm(request.POST)
        # we check if the from is valid
        if form.is_valid():
            # we get the username
            user = form.save(commit=False)
            # we making sure it is lower case
            user.username = user.username.lower()
            # we save the user
            user.save()
            # we log it in
            login(request, user)
            # we push it to home page
            return redirect('home')
        else:
            messages.error(request, 'An Error occurred during registration')


    return render(request, 'base/login_register.html', {'form':form})


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

    rooms = Room.objects.filter(
        Q(topic__name__contains=q) |
        Q(name__icontains=q) |
        Q(description__contains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, "base/home.html", context)

# Hear we will have access to what ever has been stored in pk
def room(request, pk):
    # Comment 1
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            # what ever we have entered in input(name='body') in room.html we will get there
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, "base/room.html", context)

@login_required(login_url='login')
# it called decorator and it will restrict user to enter/ and will redirect them to login page
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
@login_required(login_url='login')
def updateRoom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed hear!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    # We want to know which room we are deleting
    room = Room.objects.get(id=pk)
    # Pst method is for confirm
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        # Sending user back to home page
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    # just copied deleteRoom function
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})



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