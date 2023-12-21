from fastapi import WebSocket, WebSocketDisconnect

from .websocket import WebSocketManager


class Notifier:
    def __init__(self):
        self.webSocketManager = WebSocketManager()

    async def broadcast_message(self, message: str) -> None:
        await self.webSocketManager.broadcast(message)

    async def connect(self, websocket: WebSocket) -> None:
        await self.webSocketManager.connect(websocket)

        try:
            while True:
                print(await websocket.receive_text())
        except WebSocketDisconnect:
            self.webSocketManager.disconnect(websocket)
