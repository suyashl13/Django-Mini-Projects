import asyncio
import requests
from channels.generic.websocket import AsyncWebsocketConsumer


# TODO ADD YOUR API KEY LINE : 14

class CryptoSocket(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Connected")

        while True:
            res = requests.get(
                'https://api.nomics.com/v1/currencies/ticker?key=<your_api_key>&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&per-page=100&page=1').text
            await self.send(res)
            await asyncio.sleep(2)

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)

    async def disconnect(self, code):
        print("Client Disconnected..")
