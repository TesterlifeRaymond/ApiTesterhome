"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-02-19 22:47:14
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-02-19 22:54:42
"""


class A:
    """ test class for inherit """
    def a(self):
        """ def a for class A"""
        pass

    def b(self):
        """ def b for class A """
        pass


class B(A):
    """ test class for inherit """
    def c(self):
        """ def c for class B """
        pass

    def d(self):
        """ def d for class B """
        pass


def getmembers(klass, members=None):
    """ get a list of all class members, ordered by class """
    if members is None:
        members = []
    for k in klass.__bases__:
        print(k)
        getmembers(k, members)
    for m in dir(klass):
        print(m)
        if m not in members:
            members.append(m)
    return members

# print(A.__bases__)
# print(getmembers(A))
# print(getmembers(B))
print(getmembers(IOError))
