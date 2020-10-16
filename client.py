import websockets
import asyncio
import json
import click

URI = "ws://35.228.157.42:8000/ws"


async def sender(uri):
    while True:
        async with websockets.connect(uri) as websocket:
            inputs = input("Input message:\n")
            if inputs == '':
                break
            else:
                message = json.dumps(inputs)
                await websocket.send(message)
                reciev = await websocket.recv()
                print(reciev)


asyncio.get_event_loop().run_until_complete(sender(URI))
