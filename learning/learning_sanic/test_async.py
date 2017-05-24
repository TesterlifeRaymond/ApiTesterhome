
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-04 15:32:07
# @FileName:  test_async.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-05 18:20:33
"""
import time
import requests
import asyncio
import json
from lxml import etree
from aiohttp import ClientSession

cookies = {"no_uid": "no_uid"}

async def hello(url):
    """ pass """
    async with ClientSession(cookies=cookies) as session:
        async with session.get(url) as response:
            _response = await response.read()
            print(_response)

async def wait_download(url):
    """ pass """
    return await hello(url)    # 这里download(url)就是一个原生的协程对象
    print("get {} data complete.".format(url))

async def parse_page(url):
    """ pass """
    return await wait_download(url)
    # source = etree.HTML(html)
    # element = source.xpath('//div[@class="content"]/p/text()')
    # title = source.xpath('//h1/text()')
    # print(title)
    # return title
    # for item in element:
    #     return item

async def get_text(url):
    """ pass """
    return await parse_page(url)

async def main():
    """ pass """
    # with open('log.log', 'r') as file:
    #     urls = eval(file.read())
    tasks = []
    urls = ["http://127.0.0.1:5000/{}？u".format(item) for item in range(1, 4001)]
    for url in urls:
        task = asyncio.ensure_future(get_text(url))
        tasks.append(task)
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except TypeError as tpe:
        print(tpe)

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = []
    urls = [
        "http://182.92.178.14/model/rewrite?path=/home/fbx/dog/dog.fbx" for item in range(1, 4001)]
    for url in urls:
        task = asyncio.ensure_future(get_text(url))
        tasks.append(task)
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except TypeError as tpe:
        print(tpe)
    end = time.time()
    print("Complete in {} seconds".format(end - start))
    # loop.close()
