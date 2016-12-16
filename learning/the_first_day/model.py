"""
    这是一个model文件
"""

import requests
from bs4 import BeautifulSoup

from .util import restul_dict


class TesterHome:
    """
        这是一个TesterHome Demo Class类
    """

    def __init__(self, url, user, password):
        """
            初始化func
        :param url: testerhome的url
        :param user: username
        :param password: userpassword
        """
        self.session = requests.Session()
        self.url = url
        self.user = user
        self.password = password

    def get_pages(self):
        """
            获取初始化页面信息
        :return:
        """
        response = self.session.get(self.url).text
        return response

    def get_user(self):
        """
            获取用户登陆后的用户页面信息
        :return:
        """
        user_page = BeautifulSoup(self.get_pages(), 'lxml').find('a')
        return user_page

    @staticmethod
    def result_user_dict(my_dict):
        """
            返回格式化后的字典信息
        """
        import json
        abc_der = json.dumps(my_dict)
        return restul_dict(abc_der)

if __name__ == '__main__':
    TESTER = TesterHome('http://testerhome.com', 'liujinjia@testerlife.com', '123456')
