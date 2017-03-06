"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-02-19 23:01:53
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-02-19 23:04:53
"""

import os
for item in os.listdir('../'):
    print(item)

cwd = os.getcwd()
print(1, cwd)

os.chdir('../')
print(2, os.getcwd())

os.chdir(os.pardir)
print(3, os.getcwd())
