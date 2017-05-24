
"""
问题:
    怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？

解决方案:
    考虑下面的股票名和价格映射字典：
"""


class Calculating:
    u"""快速对字典中的数据进行运算操作的类"""
    _name = None
    _pro = None
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    @classmethod
    def min_price(cls):
        u"""字典values 排序, 返回value最小的key， value"""
        return min(zip(cls.prices.values(), cls.prices.keys()))

    @classmethod
    def max_price(cls):
        u"""字典values 排序，返回value最大的key, value"""
        return max(zip(cls.prices.values(), cls.prices.keys()))

    def max_prices(self):
        u"""字典values 排序，返回value最大的key, value"""
        return max(zip(self.prices.values(), self.prices.keys()))

    @staticmethod
    def min_prices():
        u"""字典values 排序, 返回value最小的key， value"""
        return min(zip(Calculating.prices.values(), Calculating.prices.keys()))

    @property
    def name(self):
        """ name """
        return self._name

    @name.setter
    def name(self, value):
        """set name """
        if value is not None and value is not self.name:
            self._name = value

    @property
    def get_names(self):
        """ return get names """
        return self._pro

    @get_names.setter
    def set_name(self, value):
        """ set value for _pro """
        self._pro = value

if __name__ == '__main__':
    print(Calculating.min_price())
    print(Calculating.max_price())
    print(Calculating().max_prices())
    print(Calculating.min_prices())
    Calculating.name = 'Lion'
    print(Calculating.name)
    Calculating.set_name = 'lo'
    print(Calculating.get_names)
