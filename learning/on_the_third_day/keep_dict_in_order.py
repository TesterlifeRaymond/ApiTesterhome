
"""
    问题：
        你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

    解决方案：
        为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。
        在迭代操作的时候它会保持元素被插入时的顺序，示例如下：
"""

import json
from collections import OrderedDict


def make_dict():
    """
        创建一个有顺序的dict
    :return:
    """
    my_dict = OrderedDict()
    my_dict['foo'] = '1'
    my_dict['bar'] = '2'
    my_dict['spam'] = '3'
    my_dict['grok'] = '4'

    for key in my_dict:
        print(key)
    print(json.dumps(my_dict))

if __name__ == '__main__':
    make_dict()
