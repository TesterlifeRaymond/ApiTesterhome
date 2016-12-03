
"""
    开始学习python cookbook 第三天
    并坚持规范代码规范
"""


class FindCommonalitiesInDicts:
    """
        这个class 用于在2个dict中寻找相同点
    """
    def __init__(self):
        """
            初始化两个字典
        """
        self.dict_a = {
            'x': 1,
            'y': 2,
            'z': 3
        }

        self.dict_b = {
            'w': 10,
            'y': 22,
            'z': 3
        }

    def __str__(self):
        """
        Find keys in common
        :return:
        """
        return str(self.dict_a.keys() & self.dict_b.keys())
