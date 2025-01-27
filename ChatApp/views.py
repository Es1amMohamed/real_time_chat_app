from django.shortcuts import render, redirect
from .models import Room, Message


def create_room(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_name = request.POST.get('room')

        try:
            get_room = Room.objects.get(name=room_name)
        except Room.DoesNotExist:
            new_room = Room(name=room_name)
            new_room.save()
        return redirect('chat:room', room_name=room_name, username=username)
    return render(request, 'index.html')


def massage_view(request, room_name, username):
    get_room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=get_room)
    context = {
        'room_name': get_room,
        'messages': messages,
        'user': username,
    }
    return render(request, 'message.html', context)
