
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-26 22:30:11
# @FileName:  nametuple.py
# @Project: learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-26 22:49:09
"""

import re
from collections import namedtuple


text = "foo = 1 + 3 * 4 + 6 - 10 / 2"

name = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
num = r'(?P<NUM>\d+)'
plus = r'(?P<PLUS>\+)'
times = r'(?P<TIMES>\*)'
eq = r'(?P<EQ>=)'
ws = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([name, num, plus, times, eq, ws]))
scanner = master_pat.scanner('foo=42')
# print(scanner.match())
# print(scanner.match().lastgroup, scanner.match().group())


Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    """ generate tokens function """
    scanner = pat.scanner(text)
    for match in iter(scanner.match, None):
        yield Token(match.lastgroup, match.group())


# example use generate_tokens

for token in generate_tokens(master_pat, text):
    pass

#   下面的代码告诉我们如何通过生成器表达式过滤掉所有空格标记
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
