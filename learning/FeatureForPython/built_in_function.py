
"""
@Author: liujinjia
@Date:   2017-01-19 18:00:11
@Project : doraemon
@File : built_in_function.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-01-19 18:33:57
"""


def test_abs(param):
    """
    返回一个数的绝对值。参数可以是一个整数或者一个浮点数。
    如果参数是一个复数，那么将返回它的模。
    """
    return abs(param)


def test_all(iterable):
    """
    当 iterable 中所有元素都为 True 时（或者 iterable 为空），返回 True 。相当于：

    for element in iterable:
        if not element:
            return False
        return True
    """
    return all(iterable)


def test_ascii(param):
    r"""
    返回一个输入对象的可打印的字符串，但是在返回字符串中去掉非 ASCII 编码的字符
    而这些字符在 repr() 生成的字符串中利用编码加 "\x" , "\u" 或 "\U" 前缀来表示.这个函
    数所生成的字符串与 Python2 中的 repr() 函数类似.
    """
    return param


def test_bin(interger):
    """
    将一个整数转化为一个二进制字符串。结果是一个可用的 Python 表达式。如果 x 不是
    Python 中的 int 类型，那么需要定义 __index__() 方法使之返回一个整数。
    class TestBin:
        # param is class for bin functions
        def __index__(self):
            # definition __index function for test bin class
            return 22
    """
    return bin(interger)


def main():
    """ run this file """
    print(test_abs(-1))
    print(test_all([5, 7, 11, '22', 'abc']))
    print(test_ascii('abc \nabc'))
    # print(test_bin(TestBin()))

if __name__ == '__main__':
    main()
