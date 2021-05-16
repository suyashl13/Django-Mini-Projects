from django.urls import path
from .consumer import WSConsumer

ws_patterns = [
    path('ws/some_url/', WSConsumer.as_asgi())
]
