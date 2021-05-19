from django.urls import path
from .consumer import ChatConsumer

ws_urlpatterns = [
    path('chat/<str:room_name>/', ChatConsumer.as_asgi())
]
