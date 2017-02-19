"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-02-19 22:39:47
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-02-19 22:44:54
"""


def dump(value):
    """ test dumps func """
    print(value, "=>", dir(value))

import sys
dump(0)
dump(1.0)
dump(0.0j)  # complex number
dump([])    # list
dump({})    # dictionary
dump("string")
dump(len)   # function
dump(sys)   # module
