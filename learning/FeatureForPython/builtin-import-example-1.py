"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-02-19 22:31:28
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-02-19 22:36:28
"""


import glob
import os

modules = []

for module_file in glob.glob("*tools.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        print(module_name, ext)
        module = __import__(module_name)
        modules.append(module)
        print(modules)
    except ImportError:
        pass     # ignore broken modules
# say hello to all modules
for module in modules:
    module.hello('Ray')
