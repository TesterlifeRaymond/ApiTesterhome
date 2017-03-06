"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-03-07 07:41:55
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-03-07 07:44:29
"""

# 为了将整数转换为二进制、八进制或十六进制的文本串， 可以分别使用 bin() , oct() 或 hex() 函数：

num = 1234
print(bin(num), oct(num), hex(num))

# 如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数。比如：
print(format(num, 'b'))
print(format(num, 'o'))
print(format(num, 'x'))
