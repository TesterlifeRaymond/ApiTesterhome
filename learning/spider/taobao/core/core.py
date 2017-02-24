
"""
@Author: liujinjia
@Date:   2017-02-16 16:24:34
@Project : LearningPython
@File : core.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-16 16:40:04
"""

import requests
from bs4 import BeautifulSoup


class TaoBao:
    """ get taoba items """
    session = requests.Session()
    mobile_url = 'https://world.taobao.com/search/search.htm?_ksTS=1487233624481_28&'
    'spm=a21bp.7806943.20151106.1&search_type=0&_input_charset=utf-8&navigator=all&j'
    'son=on&q=%E6%89%8B%E6%9C%BA&cna=lEcjESPdemoCAdMWkeON8TNf&callback=__jsonp_cb&a'
    'btest=_AB-LR517-LR854-LR895-PR517-PR854-PR895'
    headers = {
        "Host": "world.taobao.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/5"
        "37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

    @classmethod
    def get_all_mobile(cls):
        """ get mobile pages """
        page = cls.session.get(cls.mobile_url).text
        items = BeautifulSoup(page, 'lxml').find_all('ul', {"class": "items grid clearfix"})
        print(page)

if __name__ == '__main__':
    TaoBao.get_all_mobile()
