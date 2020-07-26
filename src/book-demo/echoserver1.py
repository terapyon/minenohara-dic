import aiohttp
from aiohttp import web
import logging

logging.basicConfig(level=logging.INFO)  #  Added
logger = logging.getLogger()  #  Added


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    ws.headers['Access-Control-Allow-Origin'] = '*'
    await ws.prepare(request)

    async for msg in ws:
        logger.info("client data")
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print("ws connection closed with exception %s" % ws.exception())

    logger.info("websocket connection closed")

    return ws


@web.middleware
async def cors_middleware(request, handler):
    response = await handler(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


app = web.Application()  #  Added
app.add_routes(
    [web.get("/ws", websocket_handler),
     web.get("/calc", cors_middleware),]
)

web.run_app(app, port=8000)
