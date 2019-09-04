
import asyncio
from aiohttp import web

from parser import parser

event_loop = asyncio.get_event_loop()


async def handle(request):
    asyncio.ensure_future(parser(timeout=10), loop=event_loop)
    text = "Hello, world"
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle), ])

web.run_app(app)

