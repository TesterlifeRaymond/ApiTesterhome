
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-25 22:28:02
# @FileName:  _type.py
# @Project: learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-25 22:35:50
"""
from functools import update_wrapper


def wrap(function):
    """ pass """
    def _wrap(*args, **kwargs):
        """ pass """
        if args:
            if args[0].__class__:
                return "class"
        return "function"
    return update_wrapper(_wrap, function)


class TestClassObject:
    """ pass """
    @wrap
    def test_function(self):
        """ pass """


@wrap
def test_function():
    """ pass """


if __name__ == '__main__':
    print(TestClassObject().test_function())
    print(test_function())
