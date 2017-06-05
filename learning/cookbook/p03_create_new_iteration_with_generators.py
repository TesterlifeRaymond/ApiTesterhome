
""" 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：
"""
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    p03_create_new_iteration_with_generators.py        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/06 06:23:56 by ray               #+#    #+#              #
#    Updated: 2017/06/06 06:23:56 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



def frange(start, stop, increment):
    """ frange func """
    number = start
    while number < stop:
        yield number
        number += increment


"""
一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 
跟普通函数不同的是，生成器只能用于迭代操作。 下面是一个实验，向你展示这样的函数底层工作机制：
"""


def countdown(num):
    """ count function """
    print("starting to count from ", num)
    while num > 0:
        yield num
        num -= 1
    print("Done")


def main():
    """ main function """
    for item in frange(0, 4, 0.5):
        print(item)

    counter = countdown(3)
    print(counter)
    print(next(counter))
    print(next(counter))
    print(next(counter))

if __name__ == '__main__':
    main()
