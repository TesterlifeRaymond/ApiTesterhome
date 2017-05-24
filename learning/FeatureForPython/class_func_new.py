
"""
@Author: liujinjia
@Date:   2017-02-20 18:32:50
@Project : LearningPython
@File : class_func_new.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-20 19:48:59
"""
import unittest

class A:
    def hello(self):
        pass

class Student(A):

    def __init__(self):
        pass

    def hello(self):
        return "hello"

    def dell(self):
        return "dell"

if __name__ == '__main__':
    doc = hasattr(Student, "hello")
    print(doc)
