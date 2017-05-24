"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-03-07 07:23:32
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-15 15:27:06
"""
from decimal import Decimal
from decimal import localcontext

"""对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可。比如："""

print(round(1.23, 1))
print(round(1.27, 1))
print(round(1.25643, 3))
"""
当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 也就是说，对1.5或者2.5的舍入运算都会得到2。
"""
print(round(1.5, 0))
print(round(2.5, 0))


first_num, second_num = 4.2, 2.1
print(first_num + second_num)


""" decimal 模块实现了IBM的”通用小数运算规范”。不用说，有很多的配置选项这本书没有提到。"""
first_num, second_num = Decimal('4.2'), Decimal('2.1')
print(first_num + second_num)
print((first_num + second_num) == Decimal('6.3'))

first_num, second_num = Decimal('1.3'), Decimal('1.7')

with localcontext() as ctx:
    ctx.prec = 3
    print(first_num / second_num)

with localcontext() as ctx:
    ctx.prec = 20
    print(first_num / second_num)
