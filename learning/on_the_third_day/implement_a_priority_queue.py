
"""
    问题:
        怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次pop操作总是返回优先级最高的那个元素

    解决方案:
        下面的类利用 heapq 模块实现了一个简单的优先级队列：
"""

import heapq


class MyQueue:
    """
        实现一个队列， MyQueue的类
    """
    def __init__(self):
        """
            初始化一个数组，用来存放items
            初始化一个_index 参数， 用于计数
        """
        self.queue = []
        self._index = 0

    def push(self, item, priority):
        """
            push func
        :param item: 需要存入队列的item
        :param priority: 位置信息
        :return:
        """
        heapq.heappush(self.queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """
            pop func
        :return: pop掉位置为最大的元素
        """
        return heapq.heappop(self.queue)[-1]

if __name__ == '__main__':
    MQ = MyQueue()
    MQ.push('abc', 0)
    MQ.push('1234', 1)
    print(MQ.queue)
    MQ.pop()
    print(MQ.queue)
