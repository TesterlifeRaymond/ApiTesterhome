
"""
@Author: liujinjia
@Date:   2017-02-08 09:41:15
@Project : LearningPython
@File : wrapper_tools.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-15 10:00:09
"""
import sys
from functools import update_wrapper


def wrapper(f):
    """ test wrapper def """
    def wrap(*args, **kwargs):
        print("func start !")
        return f(*args, **kwargs)
    return update_wrapper(wrap, f)


@wrapper
def test(name):
    """ test wrapper """
    print("hello wrapper ! my name is {0}".format(name))


class A:
    """pass"""
    @classmethod
    def a(cls):
        """pass"""
        pass

    @staticmethod
    def b():
        """pass"""
        return A.a.__qualname__.split('.')[0]

print(vars(A.b()))
