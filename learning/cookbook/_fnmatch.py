"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-03-07 06:37:20
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-03-07 06:44:27
"""

from fnmatch import fnmatch


def shell_get_param():
    """ shell get param funs"""
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    return [name for name in names if fnmatch(name, 'Dat*')]


def shell_get_addr():
    """ shell get addr """
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    return [addr for addr in addresses if fnmatch(addr, '* ST')]


if __name__ == '__main__':
    print(shell_get_addr())
