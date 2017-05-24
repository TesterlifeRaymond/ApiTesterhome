# -*- coding: utf-8 -*-
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-17 09:59:48
# @FileName:  search.py
# @Project: learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-17 11:50:26
"""

from requests import Session
from user_agent import generate_navigator
from selenium import webdriver
from lxml import etree


class Base:
    """ class base """
    def __init__(self):
        """ init """
        self.session = Session()
        self.driver = webdriver.PhantomJS()

    def request(self, method, url, body, headers=None, cookies=None):
        """ request function """
        if method == "get" or "GET":
            _request = self.session.get(url, params=body, headers=headers, cookies=cookies)
            _request.encoding = "utf-8"
            return _request.text
        return self.session.post(url, data=body, headers=headers, cookies=cookies).text

    def parser(self, html, xpath=None):
        """ pass """
        source = etree.HTML(html)
        return source.xpath(xpath)


class BaiDuSearch(Base):
    """ baidu search """
    def __init__(self):
        """ pass """
        Base.__init__(self)
        self.baidu_url = (
            "https://zhidao.baidu.com/question/1305931072525731819.html?"
            "qbpn=1_6&fr=newsearchlist&word=%E6%9D%82%E8%AF%97%E5%8D%81%"
            "E4%BA%8C%E9%A6%96&tx=wiki&uid=bd_1494815685_444&step=1"
        )

    def get_page(self):
        """ pass """
        headers = {
            "Host": "zhidao.baidu.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit"
            "/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Mobile Safari/537.36"
        }
        # page = self.request("get", self.baidu_url, "None", headers)
        # with open('page.html', 'wb') as file:
        #     file.write(page.encode())
        html = open('page.html', 'rb').read()
        print(self.parser(html.decode(), xpath='//div[@class="full-content"]/p/text()'))


if __name__ == '__main__':
    BaiDuSearch().get_page()
