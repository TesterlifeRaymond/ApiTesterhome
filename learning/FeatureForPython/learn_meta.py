
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-08 10:57:44
# @FileName:  learn_meta.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-08 14:26:53
"""


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """返回一个类对象，将属性都转为大写形式"""
    #  选择所有不以'__'开头的属性
    attrs = (
        (name, value) for name, value in future_class_attr.items() if not name.startswith('__')
    )

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr
#  这会作用到这个模块中的所有类


class Foo(object):
    """ pass """
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'

print(hasattr(Foo, 'BAR'))
# 输出: False
print(hasattr(Foo, 'bar'))
# 输出:True

f = Foo()
print(f.bar)
# 输出:'bip'
