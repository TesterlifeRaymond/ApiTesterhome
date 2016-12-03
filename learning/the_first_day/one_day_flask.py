"""
    基于pep8的代码优化
    web服用使用flask
"""
import os
import sys

from flask import Flask
from flask_restful import Api, Resource

sys.path.append(os.path.abspath(''))

APP = Flask(__name__)
API = Api(APP)


class TestFlaskApi(Resource):
    """
        定义TestFlaskApi类
    """

    @staticmethod
    def get():
        """
            该Api的get方法
        :return: Hello World !
        """
        return "Hello World !"


class TestFlaskPostApi(Resource):
    """
        定义第二条接口类：TestFlaskPostApi
    """

    @staticmethod
    def post():
        """
            该Api的post方法
        :return:  Hello World !
        """
        return "Hello World !"

if __name__ == '__main__':
    APP.run()
