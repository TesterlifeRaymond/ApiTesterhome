
"""
@Author: liujinjia
@Date:   2017-02-14 17:11:36
@Project : doraemon
@File : guest.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-16 12:11:14
"""
import random


class Guess:
    """ Guess num class """
    def __init__(self):
        """ init class """
        self.num = list(str(self.new_num()))
        self.right = self.error = 0
        self.right_list = []
        self.error_list = []

    def new_num(self):
        """ get random number """
        while 1:
            num = random.randint(1000, 9999)
            if len(set(list(str(num)))) is 4:
                return num

    def guess_num(self):
        """guess number's game """
        while 1:
            guess = input("please guess this num :")
            if list(guess) == self.num:
                return "success ! it's right ! "
            for index, param in zip(self.num, list(guess)):
                if index == param:
                    self.right_list.append(index)
                    self.right += 1
                if param in self.num and param is not index:
                    self.error_list.append(param)
                    self.error += 1
            print("{0}A{1}B".format(self.right, self.error))
            print(
                "right number is {}, "
                "error number is {}".format(
                    ''.join(self.right_list) if ''.join(self.right_list) else None,
                    ''.join(self.error_list) if ''.join(self.error_list) else None)
            )
            self.set_none()

    def set_none(self):
        """ clear list  """
        self.right = 0
        self.error = 0
        self.right_list = []
        self.error_list = []


if __name__ == '__main__':
    NUM = Guess()
    print(NUM.num)
    print(NUM.guess_num())
