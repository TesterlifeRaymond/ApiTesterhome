
"""
    问题：
        你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

    解决方案：
        通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
        假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
"""

from operator import itemgetter


ROWS = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


def rows_by_fname(arr):
    """
        按照arr的fname排序， 并返回一个arr
    :param arr:
    :return:
    """
    return sorted(arr, key=itemgetter('fname'))


def rows_by_uid(arr):
    """
        按照arr的uid排序， 并返回一个arr
    :param arr:
    :return:
    """
    return sorted(arr, key=itemgetter('uid'))


if __name__ == '__main__':
    print(rows_by_fname(ROWS))

    print(rows_by_uid(ROWS))
