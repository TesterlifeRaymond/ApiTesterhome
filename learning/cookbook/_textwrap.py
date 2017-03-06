"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-03-07 07:11:46
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-03-07 07:13:55
"""

import textwrap

"""使用 textwrap 模块来格式化字符串的输出。比如，假如你有下列的长字符串："""
TEXT = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(TEXT, 70))
