from fastapi import APIRouter, WebSocket

from app.deps import notifier

router = APIRouter()


@router.websocket_route("/manager")
async def manager_websocket_endpoint(ws_client: WebSocket) -> None:
    await notifier.connect(ws_client)
