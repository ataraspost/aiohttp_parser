
import asyncio


async def parser(url=None, timeout=0):
    print('Running in foo')
    await asyncio.sleep(timeout)
    print('Explicit context switch to foo again')