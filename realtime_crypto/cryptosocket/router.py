from django.urls import path
from .consumer import CryptoSocket

ws_urlpatterns = [
    path('crypto/', CryptoSocket.as_asgi()),
]
