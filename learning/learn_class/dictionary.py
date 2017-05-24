"""
@ Version : ??
@ Author  : liujinjia
@ File    : dictionary.py
@ Project : learning
@ Create Time: 2017-05-19 10:13
"""

my_dict = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
reload_my_dict = [my_dict[index] for index in my_dict]


KEY = "NAME AGE CLASS NUMBER"
VALUE = "RAY 30 北京皇城根小学 15"
USER_INFO = dict(zip(KEY.split(' '), VALUE.split(' ')))

print(USER_INFO.__len__())