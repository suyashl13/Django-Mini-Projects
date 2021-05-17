"""
ASGI config for realtime_crypto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter


from django.core.asgi import get_asgi_application
from cryptosocket.router import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_crypto.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
