from django.urls import re_path
from . import consumers  # Importe os consumidores que você vai criar

websocket_urlpatterns = [
    re_path(
        r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()
    ),  # Define a URL do WebSocket
]
