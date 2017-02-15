
"""
@Author: liujinjia
@Date:   2017-02-07 10:17:02
@Project : LearningPython
@File : spider_to_ganji.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-15 15:53:11
"""
import requests
from bs4 import BeautifulSoup

house = []
url = 'http://fz.ganji.com/fang1/o1/'
page = requests.get(url=url).text
parser = BeautifulSoup(page, 'lxml').findAll('div', {'class': 'f-list-item '})
for item in parser:
    title = item.find('dd', {'class': 'dd-item title'}).a.get('title')
    info = item.find('span', {'class': 'first js-huxing'}).string
    try:
        source = item.find('dd', {'class': 'dd-item source'}).span.get_text()
    except:
        pass
    print(title + ' | ' + info + ' | ' + source)
