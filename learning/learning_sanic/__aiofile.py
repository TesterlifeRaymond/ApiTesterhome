
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-03 22:33:13
# @FileName:  __aiofile.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-04 00:00:09
"""
import aiofiles
async with aiofiles.open('filename', mode='r') as f:
    contents = await f.read()
print(contents)
