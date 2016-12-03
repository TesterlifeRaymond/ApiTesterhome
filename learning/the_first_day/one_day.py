"""
        这是第一个pep8规范纠正的py文件。
        这是一个标准的py文件的头注释
"""

import os


class LearningPython:
    """
            这是LerningPython的class注释
    """

    def __init__(self, func):
        """
            这是__init__ func的def注释
        """
        self.func = func
        print(self.func.path.abspath(''))

    def os_path(self):
        """
            这是__init__ func的def注释
        """
        print(self.func.path)

    def os_help(self):
        """
            这是os_help func的注释
        :return:
        """
        return self.func

if __name__ == '__main__':
    LEARN = LearningPython(os)
    LEARN.os_path()
