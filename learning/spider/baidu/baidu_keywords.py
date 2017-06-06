
""" 通过百度keywords查询对应关键字信息 """
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    baidu_keywords.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/06 11:37:47 by ray               #+#    #+#              #
#    Updated: 2017/06/06 11:37:47 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import re
# import jieba
from requests import Session
from lxml import etree
from user_agent import generate_user_agent


class BaseClass:
    """ pass """

    def __init__(self, keywords):
        """ pass """
        self.session = Session()
        self.headers = {
            "User-Agent": generate_user_agent,
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive"
        }
        self.base_url = 'http://baidu.com/s?'
        self.key_words = 'ie=utf-&wd={}&rn=50'.format(keywords)

    def request(self, url):
        """ request function """
        response = self.session.get(url)
        response.encoding = 'utf-8'
        return response.content

    @staticmethod
    def parser(html, xpath):
        """ parser pages source """
        html = re.sub('<em>|</em>|<em class>', '', html)
        source = etree.HTML(html)
        return source.xpath(xpath)

    def output(self, url, xpath):
        """ return html tags """
        return self.parser(self.request(url).decode(), xpath)

class BaiDuSpider(BaseClass):
    """ 百度keywords爬虫 """
    def __init__(self, keywords):
        """ init class """
        BaseClass.__init__(self, keywords)

    def _output(self):
        """ pass """
        return self.output(self.base_url + self.key_words, '//div[@class="result c-container "]')

def main():
    """ pass """
    search = BaiDuSpider('全民枪战')
    for item in search._output():
        text = item.xpath('h3[@class="t"]/a/text()')
        if text:
            print(text[0])
        # print(', '.join(jieba.lcut_for_search(item.xpath('h3[@class="t"]/a/text()')[0])))

if __name__ == '__main__':
    main()
