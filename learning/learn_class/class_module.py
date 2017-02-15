
"""
@Author: liujinjia
@Date:   2017-02-15 17:23:25
@Project : LearningPython
@File : class_module.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-15 18:33:56
"""


class ClassModule:
    """ test class module
    深入理解python class中的内置函数应用
    """
    def __init__(self, name):
        """ class 的初始化函数 """
        self.name = name

    def __str__(self):
        """ class str , 当class被直接调用时返回"""
        return "class module name is {0}".format(ClassModule.__name__)

    def __dict__(self):
        """ class __dict__ module """
        return ClassModule.__dict__

    def __repr__(self):
        """ class module repr func
        if __str__ method is not defined , __str__ == __repr__
        """
        return "class module is A"

    def print_hello_world(self):
        """ print new class hello func """
        return "hello {0} world".format(ClassModule.__name__)


class NewClass(ClassModule):
    """ new class 继承 class module """
    def __init__(self):
        """ modify class module init func """
        pass

    def __str__(self):
        """ return str module """
        return NewClass.__name__

    def __dict__(self):
        """ return new class __dict__
        If this method is not defined， return ClassModule.__dict__
        """
        return NewClass.__dict__

    def __module__(self):
        """ new class module func """
        return NewClass.__module__

    def print_hello(self):
        """ print new class hello func """
        return "hello {0}".format(NewClass.__name__)


def main():
    """ run script """
    obj = ClassModule('Ray')
    print(obj.name)     # Ray
    print(obj)  # class module name is ClassModule
    print(obj.__dict__())
    new = NewClass()
    print(new)  # NewClass
    print(new.__dict__())
    print(new.__module__())
    print(new.print_hello())
    print(new.print_hello_world())


if __name__ == '__main__':
    main()
