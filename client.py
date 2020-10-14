import websockets
import asyncio


async def sender(uri):
    async with websockets.connect(uri) as websocket:
        message = input("Input message")
        await websocket.send(message)
        reciev = await websocket.recv()
        print(reciev)


asyncio.get_event_loop().run_until_complete(sender("ws://35.228.157.42:8000/ws"))