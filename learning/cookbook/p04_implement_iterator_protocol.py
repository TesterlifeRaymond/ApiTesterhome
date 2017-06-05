
""" 你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数。 在4.2小节中，
使用Node类来表示树形数据结构。你可能想实现一个以深度优先方式遍历树形节点的生成器。 下面是代码示例：
"""
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    p04_implement_iterator_protocol.py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/06 06:49:10 by ray               #+#    #+#              #
#    Updated: 2017/06/06 06:49:10 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Node:
    """ node class """
    def __init__(self, value):
        """ pass """
        self.__value = value
        self.children = []

    def __repr__(self):
        """ pass """
        return "Node({!r})".format(self.__value)

    def add_child(self, node):
        """ add children """
        self.children.append(node)

    def __iter__(self):
        """ return iter obj """
        return iter(self.children)

    def depth_first(self):
        """ depth first """
        print("self", self)
        yield self
        for item in self:
            yield from item.depth_first()


def main():
    """ pass """
    root = Node(0)
    child_one = Node(1)
    child_two = Node(2)
    root.add_child(child_one)
    root.add_child(child_two)
    child_one.add_child(Node(3))
    child_one.add_child(Node(4))
    child_two.add_child(Node(5))

    for item in root.depth_first():
        print(item)

if __name__ == '__main__':
    main()
