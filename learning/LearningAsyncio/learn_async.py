
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-07 14:51:24
# @FileName:  learn_async.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-15 15:42:11
"""
import types


def wrap(func):
    """ wrap """
    def _wrap(*args, **kwargs):
        """ return func """
        print("start .....")
        result = func(*args, **kwargs)
        print("end .....")
        return result
    return _wrap


@wrap
def name():
    """ print user name """
    print('Ray')


@wrap
def age():
    """ print user age """
    print(18)


async def asy_name():
    """ async func """
    print('Ray')
    await switch()
    print('Raymond')
    await switch()
    print('行者')


async def asy_age():
    """ async age """
    age = 0
    print(age)
    age = 25
    await switch()
    print(age + 5)
    await switch()
    return age + 10

name, age = asy_name(), asy_age()


@types.coroutine
def switch():
    """ switch func """
    yield


def try_cache(param):
    """ try StopIteration """
    print(dir(param))
    try:
        print(param.__qualname__)
        param.send(None)
    except StopIteration:
        pass


@wrap
async def main():
    """ main func """
    await age
    await name


def run(_list):
    """ run async funcs """
    _list = list(_list)
    while 1:
        for item in _list:
            try:
                item.send(None)
            except StopIteration:
                _list.remove(item)
        if len(_list) == 0:
            break

case = run([name, age])
