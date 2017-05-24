
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-15 15:56:44
# @FileName:  neihanduanzi.py
# @Project: learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-15 18:04:57
"""
# import requests
import time
from requests import Session
# import gevent
from lxml import etree
from functools import update_wrapper
session = Session()
headers = {
    "Referer": "http://m.neihanshequ.com/?is_json=1&app_name=neihanshequ_web&max_time=1494841820"
               "&csrfmiddlewaretoken=f21fbb8d66ed33440fae0609b3d3f9fc"}


class Wrapper:
    """ pass """
    def __init__(self, encoding=None):
        """ pass """
        if encoding is None:
            self.param = 'utf-8'
        self.param = encoding

    def __call__(self, function):
        """ pass """
        def parse(*args, **kwargs):
            """ pass """
            func = function(*args, **kwargs)
            if isinstance(func, str):
                return func
            xpath = kwargs.get('xpath')
            if xpath is None:
                req = session.get(args[0]).json()
                return req
            func.encoding = self.param
            print(func.text)
            source = etree.HTML(func.text)
            resp = source.xpath(xpath)
            return resp
        return update_wrapper(parse, function)


@Wrapper(encoding='utf-8')
def request(url, xpath=None):
    """ request funtions
    :type xpath: object
    """
    return session.get(url)

if __name__ == '__main__':
    comment = []
    url = (
        "http://m.neihanshequ.com/?is_json=1&app_name=neihanshequ_web&max_time=1434841589&csrfmiddlewaretoken=f21fbb8d66ed33440fae0609b3d3f9fc&is_json=1&app_name=neihanshequ_web&max_time=&csrfmiddlewaretoken=8aeb29430f7b3f53a93ac077a68f1e90"
    )
    cookies = dict(
        uuid="w:e6029445f8d941539cc00eb7363b969c",
        tt_webid="58370939716",
        csrftoken="8aeb29430f7b3f53a93ac077a68f1e90",
        skip_guidence="1",
        _ga="GA1.2.667380712.1494841880",
        _gid="GA1.2.846470712.1494841880",
        _gat="1"
    )
    print(url)
    data = session.get(url, headers=headers, cookies=cookies).json()
    print(data)
    for item in data.get('data').get('data'):
        print(item.get('group').get('content'))


    # for item in request(url, xpath='//li[@class="share-wrapper right"]'):
    #     for page_num in range(0, 200, 20):
    #         comment.append(
    #             "http://neihanshequ.com/m/api/get_essay_comments/?group_id={}"
    #             "&app_name=neihanshequ_web&offset={}".format(item.values()[1], page_num)
    #         )
    #     print("**********************************")
    #     print(item.values()[3])
    #     print("**********************************")

    # print(len(comment))
    # events = [gevent.spawn(request, url) for url in comment]
    # gevents = gevent.joinall(events)
    # for item in gevents:
    #     for _value in item.value.get('data').get('recent_comments'):
    #         print(item.value.get('group_id'), _value.get('text'))

    # data = request(url, xpath=None)
    # for text in data.get('data').get('recent_comments'):
    #     print(text.get('text'))
