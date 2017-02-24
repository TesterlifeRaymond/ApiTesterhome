
"""
@Author: liujinjia
@Date:   2017-02-16 16:41:22
@Project : LearningPython
@File : youku.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-16 16:57:54
"""

import requests
from bs4 import BeautifulSoup


class YouKu:
    """ get you ku web """
    session = requests.Session()
    home_url = 'http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A'

    @classmethod
    def get_pages(cls, url=None):
        """ get web page """
        if url is None:
            page = cls.session.get(cls.home_url)
        page.encoding = 'utf-8'
        return page.text

    @classmethod
    def parse_pages(cls, html=None):
        """ parse some pages """
        if html is None:
            parse = BeautifulSoup(cls.get_pages(), 'lxml').findAll('div', {"class": "yk-box"})
        return parse

    @classmethod
    def parse_guess_movies(cls):
        """ get guess me like movies """
        for item in cls.parse_pages():
            if item.a is not None and item.a.get('title') is not None:
                print(item.a.get('title'), item.a.get('href'))


if __name__ == '__main__':
    YouKu.parse_guess_movies()
