import websockets
import asyncio
import json

reg_mes = {"type": "register_user",
           "data": {"user": [{
               "password": "Qwerty12345",
               "login": "User11",
               "email": "User11@user.com",
               "username": "User11"
           }], "meta": None},
           "jsonapi": {
               "version": "1.0"
           }}


async def sender():
    async with websockets.connect('ws://127.0.0.1:8000/ws') as websocket:
        message = json.dumps(reg_mes)
        await websocket.send(message)
        a = await websocket.recv()
        print(a)


if __name__ == '__main__':
    asyncio.run(sender())
