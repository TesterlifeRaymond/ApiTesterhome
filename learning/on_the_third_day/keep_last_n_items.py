
"""
    问题:
        在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

    解决方案:
        保留有限历史记录正是 collections.deque
        大显身手的时候。比如，下面的代码在多行上面做简单的文本匹配， 并返回匹配所在行的最后N行：
"""


from collections import deque


def search(lines, pattern, history=5):
    """
        文本匹配函数
    :param lines:
    :param pattern:
    :param history:
    :return:
    """
    previous_lines = deque(maxlen=history)
    for _ in lines:
        if pattern in _:
            yield _, previous_lines
        previous_lines.append(_)


def deque_demo():
    """
    使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
    当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
    :rtype: object
    :return:
    """
    q = deque(maxlen=2)
    [q.append(_) for _ in range(2)]
    print(q)
    q.append(2)
    print(q)
    q.append(3)
    print(q)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prev_lines in search(f, 'python', 5):
            for _ in prev_lines:
                print(_, end='')
            print(line, end='')
            print('-' * 20)

    deque_demo()
