
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-03 20:11:23
# @FileName:  __init__.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-08 10:21:45
"""
import requests
from unittest import TestCase, main


class DouBanApi(TestCase):
    """ pass """

    def test_douban_bookinfo(self):
        """ pass """
        api_url = 'https://api.douban.com/v2/book/1220562'
        print(requests.get(api_url).json())

if __name__ == '__main__':
    main()
