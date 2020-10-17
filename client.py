import websockets
import asyncio
import json
import click

URI = "ws://35.228.157.42:8000/ws"


async def sender(uri):
    while True:
        async with websockets.connect(uri) as websocket:
            inputs = input("Input message (Enter to exit):\n")
            if inputs == '':
                # hard stop enventloop
                asyncio.get_event_loop().stop()
            else:
                message = json.dumps(inputs)
                await websocket.send(message)
                try:
                    await websocket.recv()
                except websockets.exceptions.ConnectionClosedOK as error:
                    print("Connections close: ", error)


asyncio.get_event_loop().run_until_complete(sender(URI))
