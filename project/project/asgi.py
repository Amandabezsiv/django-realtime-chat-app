"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Importe o roteamento do app de chat

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nome_do_seu_projeto.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Para requisições HTTP padrão
        "websocket": AuthMiddlewareStack(  # Para conexões WebSocket
            URLRouter(
                chat.routing.websocket_urlpatterns  # Adicione os padrões de URL do chat
            )
        ),
    }
)
