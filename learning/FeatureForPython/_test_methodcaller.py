
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-28 18:28:16
# @FileName:  _test_methodcaller.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-15 15:30:27
"""


class Methodcaller:
    """
    Return a callable object that calls the given method on its operand.
    After f = methodcaller('name'), the call f(r) returns r.name().
    After g = methodcaller('name', 'date', foo=1), the call g(r) returns
    r.name('date', foo=1).
    """
    __slots__ = ('_name', '_args', '_kwargs')

    def __init__(*args, **kwargs):
        """" pass """
        if len(args) < 2:
            msg = "methodcaller needs at least one argument, the method name"
            raise TypeError(msg)
        self = args[0]
        self._name = args[1]
        if not isinstance(self._name, str):
            raise TypeError('method name must be a string')
        self._args = args[2:]
        self._kwargs = kwargs

    def __call__(self, obj):
        """ pass """
        return getattr(obj, self._name)(*self._args, **self._kwargs)

    def __repr__(self):
        """ pass """
        args = [repr(self._name)]
        args.extend(map(repr, self._args))
        args.extend('%s=%r' % (k, v) for k, v in self._kwargs.items())
        return '%s.%s(%s)' % (self.__class__.__module__,
                              self.__class__.__name__,
                              ', '.join(args))


@Methodcaller
def function():
    """ pass """
    pass


if __name__ == '__main__':
    print(function)
