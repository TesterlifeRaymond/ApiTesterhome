
"""
    使用 collections 模块中的 defaultdict 来构造一个按照参数传入顺序排序的dict
"""


from collections import defaultdict


def defaultdict_list():
    """
        使用defaultdict 生成一个list
    :return:
    """
    m_d = defaultdict(list)
    _ = [m_d['a'].append(i) for i in range(1, 4)]
    print(m_d)


def defaultdict_set():
    """
        使用defaultdict 生成一个set
    :return:
    """
    m_s = defaultdict(set)
    _ = [m_s['a'].add(i) for i in range(1, 4)]
    print(m_s)


def setdefault_dict():
    """
        需要注意的是， defaultdict 会自动为将要访问的键(就算目前字典中并不存在这样的键)创建映射实体。
        如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：
    :return:
    """
    m_d = {}  # A regular dictionary
    m_d.setdefault('a', []).append(1)
    m_d.setdefault('a', []).append(2)
    m_d.setdefault('b', []).append(4)
    print(m_d)


def make_dict():
    """
        使用defaultdict(list) 快速创建一个字典
    :return:
    """
    my_dict = defaultdict(list)
    my_list = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    for key, value in enumerate(my_list):
        my_dict[key].append(value)
    print(my_dict)


if __name__ == '__main__':
    defaultdict_list()
    defaultdict_set()

    setdefault_dict()
    make_dict()
