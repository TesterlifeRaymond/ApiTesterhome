
"""
@Author: liujinjia
@Date:   2017-02-07 10:17:02
@Project : LearningPython
@File : spider_to_qiubai.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-07 10:47:13
"""

import requests
from bs4 import BeautifulSoup


def qiu_shi_bai_ke():
    """ get qiu bai 's page to parser """
    url = 'http://www.qiushibaike.com/'
    page = requests.get(url).text
    parse = BeautifulSoup(page, 'lxml').findAll('div', {'class': 'content'})
    for item in parse:
        print(item.get_text())


def ganji():
    """ get gan ji 's page to parser """
    url = 'http://fz.ganji.com/fang1/o1/'
    page = requests.get(url).text
    parser = BeautifulSoup(page, 'lxml').find_all('div', {"class": "f-list-item"})
    for item in parser:
        print(item.img.attrs)
