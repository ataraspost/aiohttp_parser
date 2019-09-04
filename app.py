
import asyncio
from aiohttp import web

from parser import parser

event_loop = asyncio.get_event_loop()


async def handle(request):
    try:
        data = await request.post()
        asyncio.ensure_future(parser(**data), loop=event_loop)
    except:
        return web.json_response({'status': 'error'})
    return web.json_response({'status': 'ok'})

app = web.Application()
app.add_routes([web.post('/', handle), ])

web.run_app(app)

