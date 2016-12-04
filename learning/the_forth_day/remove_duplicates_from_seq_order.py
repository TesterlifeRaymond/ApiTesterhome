
"""
    问题:
        怎样在一个序列上面保持元素顺序的同时消除重复的值？

    解决方案:
        如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。比如：
"""


def dedupe_list(items: list) -> object:
    """
        如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题

    :rtype: iterable
    :param items:
    :return:
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_dict(items: dict, key=None) -> object:
    """
        dedupe_list 方法仅仅在序列中元素为 hashable 的时候才管用。
        如果你想消除元素不可哈希(比如 dict 类型)的序列中重复元素的话，你需要将上述代码稍微改变一下，就像这样：
    :rtype: iterable
    :param key:
    :param items:
    :return:
    """

    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)


def remove_same(items):
    """
        如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合。比如：
    :param items:
    :return:
    """

    return set(items)

if __name__ == '__main__':
    L = [1, 5, 2, 1, 9, 1, 5, 10]
    # noinspection PyTypeChecker
    print(list(dedupe_list(L)))

    D = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    # noinspection PyTypeChecker
    print(list(dedupe_dict(D, key=lambda key: key['y'])))

    print(remove_same(L))
