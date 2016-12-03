

"""
    这是一个递归函数, 主要用于深度json的解析
    例： dict([list,[dict,[dict]]])
"""

DATA = {}


def get_value(my_dict, key):
    """
        这是一个递归函数
    """

    if isinstance(my_dict, dict):
        if my_dict.get(key):
            return my_dict[key]

        for my_dict_key in my_dict:
            if get_value(my_dict[my_dict_key], key):
                return get_value(my_dict[my_dict_key], key)

    if isinstance(my_dict, list):
        for my_dict_arr in my_dict:
            if get_value(my_dict_arr, key):
                return get_value(my_dict_arr, key)


if __name__ == '__main__':
    print(get_value(DATA, "pageCount"))
