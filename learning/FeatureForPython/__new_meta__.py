
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-08 14:30:55
# @FileName:  __new_meta__.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-08 16:25:06
"""


class TestMetaClass:
    """pass"""
    pass


def echo_bar(cls, index):
    """pass"""
    return cls.__bases__[index].__doc__

if __name__ == '__main__':
    Ray = type('Ray', (TestMetaClass,), {"echo_bar": echo_bar, "__doc__": "这是一个测试元类的class"})
    print(Ray.echo_bar(Ray, 0))
