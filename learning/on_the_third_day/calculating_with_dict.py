
"""
    问题:
        怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？

    解决方案:
        考虑下面的股票名和价格映射字典：
"""


class Calculating:
    """
        快速对字典中的数据进行运算操作的类
    """
    def __init__(self):
        self.prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

    def min_price(self):
        """
            字典values 排序, 返回value最小的key， value
        :return:
        """
        return min(zip(self.prices.values(), self.prices.keys()))

    def max_price(self):
        """
            字典values 排序，返回value最大的key, value
        :return:
        """
        return max(zip(self.prices.values(), self.prices.keys()))


if __name__ == '__main__':
    C = Calculating()
    print(C.min_price())
    print(C.max_price())