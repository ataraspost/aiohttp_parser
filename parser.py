
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0'}


async def parser(url=None, timeout=0, instance_id=None):
    await asyncio.sleep(int(timeout))
    data = await get_result(url)
    data['instance_id'] = instance_id
    requests.post('http://localhost:8000/result/', data=data)


async def get_result(url):
    response = await get_html(url)
    soup = BeautifulSoup(response, 'html.parser')
    data = {}

    try:
        data['title'] = soup.title.get_text()
    except:
        data['title'] = 'error'

    try:
        data['h1'] = list()
        for item in soup.find_all('h1'):
            data['h1'].append(item.get_text())
        data['h1'] = ', '.join(data['h1'])
    except:
        data['h1'] = 'error'

    try:
        data['string_encoding'] = get_encoding(soup)
    except:
        data['string_encoding'] = 'error'

    return data

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as resp:
            return await resp.text()

def get_encoding(soup):
    encod = soup.meta.get('charset')
    if encod == None:
        encod = soup.meta.get('content-type')
        if encod == None:
            content = soup.meta.get('content')
            match = re.search('charset=(.*)', content)
            if match:
                encod = match.group(1)
            else:
                raise ValueError('unable to find encoding')
    return encod

