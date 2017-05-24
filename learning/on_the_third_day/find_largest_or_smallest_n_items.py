
""" 怎样从一个集合中获得最大或者最小的N个元素列表？"""

import heapq
from collections import Counter


def heapq_list_demo():
    """
    这是一个heapq的demo
    heapq.nlargest(位数, list)
    heapq.nsmallest(位数, list)
    """
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(Counter(nums).most_common(2))
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))


def heapq_dict_demo():
    """
        这是一个heapq的demo
        与上一个demo不同的是， 这次是对一个list中的多个dict内容按照某个value
            进行排序
    :return:
    """
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    cheap = heapq.nsmallest(len(portfolio), portfolio, key=lambda key: key['price'])
    expensive = heapq.nlargest(len(portfolio), portfolio, key=lambda key: key['price'])
    print(cheap)
    print(expensive)


def heapq_heappop_demo():
    """
        这是一个对快速删除list最小参数的方法
         heapq.heapify(list)
            且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到， 该方法会先将第一个元素弹出来，
            然后用下一个最小的元素来取代被弹出元素(这种操作时间复杂度仅仅是O(log N)，N是堆大小)
    :return:
    """
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.heapify(nums)

    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))

if __name__ == '__main__':
    heapq_list_demo()
