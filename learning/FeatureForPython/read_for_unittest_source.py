
"""
@Author: liujinjia
@Date:   2017-01-20 16:56:56
@Project : doraemon
@File : read_for_unittest_source.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-07 14:16:28
"""


from posix import _have_functions


def wrapper(func):
    """ wrapper """
    def function(*args, **kwargs):
        """ wrapper functions """
        args[0].hello()
        return func(*args, **kwargs)
    return function


class Demo:
    """ test wrapper work type """
    @wrapper
    def hi(self, name):
        """ hi function """
        print("hi")
        print(name)

    @staticmethod
    def hello():
        """ no wrapper , hello function """
        print("hello")


def _exists(name):
    """ return name is in globals() result """
    return name in globals()

def test_os_functions():
    """ test functions for os add some thing func """
    if _exists("_have_functions"):
        _globals = globals()

        def _add(param, fn):
            if (fn in _globals) and (param in _have_functions):
                _set.add(_globals[fn])

        _set = set()
        _add("HAVE_FACCESSAT", "access")
        _add("HAVE_FCHMODAT", "chmod")
        _add("HAVE_FCHOWNAT", "chown")
        _add("HAVE_FSTATAT", "stat")
        _add("HAVE_FUTIMESAT", "utime")
        _add("HAVE_LINKAT", "link")
        _add("HAVE_MKDIRAT", "mkdir")
        _add("HAVE_MKFIFOAT", "mkfifo")
        _add("HAVE_MKNODAT", "mknod")
        _add("HAVE_OPENAT", "open")
        _add("HAVE_READLINKAT", "readlink")
        _add("HAVE_RENAMEAT", "rename")
        _add("HAVE_SYMLINKAT", "symlink")
        _add("HAVE_UNLINKAT", "unlink")
        _add("HAVE_UNLINKAT", "rmdir")
        _add("HAVE_UTIMENSAT", "utime")
        print(_set)


class Staticmethod:
    """ test statcimethod class """

    def __get__(self, *args, **kwargs):     # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, function):   # real signature unknown; restored from __doc__
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """ class __new__ funcs """
        pass

    __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


if __name__ == '__main__':
    test_os_functions()
    print(Staticmethod.__new__())
