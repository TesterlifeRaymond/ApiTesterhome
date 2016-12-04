
"""
    问题:
        怎样找出一个序列中出现次数最多的元素呢？

    解决方案:
        collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。
"""


from collections import Counter


WORDS = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]


def words_counter(items):
    """
        一个list中每个元素总数的计数器
    :param items:
    :return:
    """
    return Counter(items)


def words_most_counter(items):
    """
        返回出现频率最高的3个单词
    :param items:
    :return:
    """
    return Counter(items).most_common(3)

if __name__ == '__main__':
    print(words_counter(WORDS))

    print(words_most_counter(WORDS))

    # 作为输入， Counter 对象可以接受任意的由可哈希(hashable)元素构成的序列对象。
    # 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。比如：
    print(Counter(WORDS)['eyes'])


"""
    Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。比如：

    >>> a = Counter(words)
    >>> b = Counter(morewords)
    >>> a
    Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
    "you're": 1, "don't": 1, 'under': 1, 'not': 1})
    >>> b
    Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
    'my': 1, 'why': 1})
    >>> # Combine counts
    >>> c = a + b
    >>> c
    Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
    'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
    'looking': 1, 'are': 1, 'under': 1, 'you': 1})
    >>> # Subtract counts
    >>> d = a - b
    >>> d
    Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
    "you're": 1, "don't": 1, 'under': 1})
"""
