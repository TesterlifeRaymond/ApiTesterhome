"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-03-07 07:05:08
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-03-07 07:10:09
"""

import sys


def sub(text):
    """ 可以将变量替换步骤用一个工具函数封装起来 """
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


class SafeSub(dict):
    """防止key找不到"""

    def __missing__(self, key):
        """ missing funcs """
        return '{' + key + '}'

if __name__ == '__main__':
    # name, num = 'Ray', '38'
    name = 'Ray'
    text = '{name}  has {num} messages'
    print(sub(text))
