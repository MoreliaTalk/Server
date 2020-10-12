# ************** Standart module *********************
from datetime import datetime
# ************** Standart module end *****************


# ************** External module *********************
from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect
# ************** External module end *****************


# Server instance creation
app = FastAPI()


# Save clients session
# TODO: Нужно подумать как их компактно хранить
clients = []


# Chat websocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        try:
            data = await websocket.receive_json()
            client = controller.ProtocolMethods(data)
            await websocket.send_json(client.get_response(), mode='binary')
        except WebSocketDisconnect as error:
            clients.remove(websocket)
            break
        except RuntimeError as error:
            clients.remove(websocket)
            break
        else:
            if websocket.client_state.value == 0:
                await websocket.close(code=1000)
                clients.remove(websocket)


if __name__ == "__main__":
    app