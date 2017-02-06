#-*- coding: utf-8 -*-

"""
    问题:
        你想排序类型相同的对象，但是他们不支持原生的比较操作。

    解决方案:
        内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给它，
        这个 callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序这些对象。
        比如，如果你在应用程序里面有一个 User 实例序列，并且你希望通过他们的 user_id 属性进行排序，
        你可以提供一个以 User 实例作为输入并输出对应 user_id 值的 callable 对象。比如：
"""

from operator import attrgetter

class User:
    """
        接收一个userid，如果被调用则返回这个userid
    """

    def __init__(self, user_id):
        """
            User类的init函数，来初始化这个类的user_id
        """
        self.user_id = user_id

    def __repr__(self):
        return 'User({0})'.format(self.user_id)


def sort_notcompare():
    """
        这是User类的排序方法
        重点: users的传入方式及key排序的用法
    """
    users = [User(23), User(3), User(56)]
    print(sorted(users, key=lambda u: u.user_id))


def operator_by_attrgetter():
    """
        通过operator.attrgetter() 进行排序
    """
    users = [User(46), User(23), User(122)]
    print(sorted(users, key=attrgetter('user_id')))


def min_max_attrgetter():
    """ 
        该小结用到的计数同样适用于像min(),max()之类的函数
    """
    users = [User(23), User(3), User(56)]
    print(min(users, key=lambda key: key.user_id))
    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=lambda key: key.user_id))
    print(max(users, key=attrgetter('user_id')))

if __name__ == '__main__':
    sort_notcompare()
    operator_by_attrgetter()
    min_max_attrgetter()
