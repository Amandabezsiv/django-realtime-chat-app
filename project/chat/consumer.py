import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"][
            "room_name"
        ]  # Pega o nome da sala da URL
        self.room_group_name = "chat_%s" % self.room_name  # Define um grupo de sala

        # Junta-se ao grupo da sala
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()  # Aceita a conexão WebSocket

    async def disconnect(self, close_code):
        # Deixa o grupo da sala
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)  # Recebe a mensagem como JSON
        message = text_data_json["message"]

        # Envia a mensagem para o grupo da sala
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({"message": message}))
