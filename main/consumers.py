import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class AtcConsumer(WebsocketConsumer):
    async def connect(self):
        print("connection")
        self.room_group_name = "test_room"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        print("Disconnected", code)