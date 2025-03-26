from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from .models import Area, Promotion

class BeaconConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs'].get('user_id', 'anon')
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        major = data.get('major')
        if major:
            area = await self.get_area(major)
            if area:
                promo = await self.get_promo(area)
                if promo:
                    await self.send(text_data=json.dumps({
                        'area': area.name,
                        'content': promo.content
                    })))

    @database_sync_to_async
    def get_area(self, major):
        try:
            return Area.objects.get(major=major)
        except Area.DoesNotExist:
            return None

    @database_sync_to_async
    def get_promo(self, area):
        try:
            return Promotion.objects.filter(area=area, active=True).first()
        except Promotion.DoesNotExist:
            return None