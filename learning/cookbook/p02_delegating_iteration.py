
""" 你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。 你想直接在你的这个新容器对象上执行迭代操作。
实际上你只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上去"""

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    p02_delegating_iteration.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/06 06:24:14 by ray               #+#    #+#              #
#    Updated: 2017/06/06 06:24:14 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Node:
    """ class node """
    def __init__(self, value):
        """ init func """
        self._value = value
        self.children = []

    def __repr__(self):
        """ class repr func """
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        """ add children func """
        self.children.append(node)

    def __iter__(self):
        """ class iter property """
        return iter(self.children)

def main():
    """ main function"""
    node = Node("Ray")
    print(node)
    node.add_child("LiLei")
    node.add_child("liaoxuefeng")
    _iter = iter(node)
    print(next(_iter))
    print(next(_iter))


"""
Python的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象。 
如果你只是迭代遍历其他容器的内容，你无须担心底层是怎样实现的。你所要做的只是传递迭代请求既可。
这里的 iter() 函数的使用简化了代码， iter(s) 只是简单的通过调用 s.__iter__() 方法来返回对应的迭代器对象，
就跟 len(s) 会调用 s.__len__() 原理是一样的。
"""

if __name__ == '__main__':
    main()
