"""
    公用util模块
"""


def restul_dict(my_dict):
    """
        获取一个dict 返回dict中的id
    :param my_dict: 一个字典
    :return: id信息 or none
    """
    return my_dict.get('id', "not id param")

print(restul_dict(dict(id=13, name='liu', password='123456')))
print(restul_dict(dict(name='Ray', password='654321')))
print(restul_dict(dict(a="b", c="d")))
