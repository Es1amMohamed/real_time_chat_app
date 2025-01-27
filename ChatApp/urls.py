from django.urls import path
from . import views



app_name = 'chat'

urlpatterns = [
    path('', views.create_room, name='create_room'),
    path('<str:room_name>/<str:username>/', views.massage_view, name='room'),
]