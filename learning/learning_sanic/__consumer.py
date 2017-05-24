
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-04 11:35:20
# @FileName:  __consumer.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-05 17:48:25
"""


import asyncio
import threading
from aiohttp import ClientSession


async def urls():
    """ pass """
    return await 'http://httpbin.org/headers'

async def hello(url):
    """ pass """
    print(url)
    async with ClientSession() as session:
        async with session.get(url) as response:
            _response = await response.read()
            print(_response)

if __name__ == '__main__':
    from time import time
    start = time()
    loop = asyncio.get_event_loop()
    urls = ['http://10.10.146.171:5000/{}'.format(i) for i in range(4001)]
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(hello(url))
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    print('end time : {}'.format(time() - start))
