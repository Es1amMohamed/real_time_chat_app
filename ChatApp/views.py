from django.shortcuts import render
from .models import Room, Message


def create_room(request):
    return render(request, 'index.html')


def massage_view(request, room_id, username):
    return render(request, 'message.html')
