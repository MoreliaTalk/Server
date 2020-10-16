import websockets
import asyncio
import json


async def sender(uri):
    async with websockets.connect(uri) as websocket:
        message = input("Input message:\n")
        await websocket.send(json.dumps(message))
        reciev = await websocket.recv()
        print(reciev)


#asyncio.get_event_loop().run_until_complete(sender("ws://35.228.157.42:8000/ws"))