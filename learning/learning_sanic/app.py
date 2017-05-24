
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-03 20:11:32
# @FileName:  app.py
# @Project: Learning
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-15 14:55:24
"""

from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)


@app.route('/')
async def hello(request):
    """ pass """
    return text('hello world !')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
