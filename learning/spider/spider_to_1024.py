
"""
@Author: liujinjia
@Date:   2017-02-15 13:52:42
@Project : LearningPython
@File : spider_to_1024.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-15 15:49:05
"""

import requests
from bs4 import BeautifulSoup


class Spider:
    """ 1024 img spider """
    start_url = 'http://www.dxlymm.com/thread0806.php?fid=5'
    session = requests.Session()

    @classmethod
    def get_home_page(cls, url=None):
        """ get 1024 img page """
        if url is None:
            page = cls.session.get(cls.start_url)
        else:
            page = cls.session.get(url)
        page.encoding = 'gbk'
        return page.text

    @classmethod
    def parse_pages(cls):
        """ parse 1024 pages """
        parse = BeautifulSoup(cls.get_home_page(), 'lxml')
        parse = parse.findAll('tr')
        return parse

    @classmethod
    def get_uri_list(cls):
        """ get parse list url """
        uri_list = []
        for item in cls.parse_pages():
            if item.h3 is not None:
                # print(item.h3.a.get('href'), item.h3.a.string)
                uri_list.append("http://www.dxlymm.com/" + item.h3.a.get('href'))
        return uri_list

    @classmethod
    def get_seed_page(cls):
        """ get pages seeds """
        page = cls.get_home_page(cls.get_uri_list()[11])
        return BeautifulSoup(page, 'lxml').find('a', {"target": "_blank"}).string

    @classmethod
    def get_seed(cls):
        """ get seeds
        http://www.rmdown.com/download.php?ref=163b9b55fba74fbc988124acb4db8b23bbc739bf55e&reff=MTQ4NzE0NDcwOA%3D%3D&submit=download
        this func get some element
        <INPUT size=58 name="ref" value="163b9b55fba74fbc988124acb4db8b23bbc739bf55e"
        style="font-size:10px;"><INPUT TYPE="hidden" NAME="reff" value="MTQ4NzE0NDU2Nw=="><BR>

        get this tags , value and value splicing into url， download seeds！
        """
        page = cls.get_home_page(cls.get_seed_page())
        print(page)


if __name__ == '__main__':
    print(Spider.get_seed())
