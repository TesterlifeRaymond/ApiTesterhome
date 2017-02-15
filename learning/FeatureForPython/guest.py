
"""
@Author: liujinjia
@Date:   2017-02-14 17:11:36
@Project : doraemon
@File : guest.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-15 12:15:33
"""
import random
NUM = None


def new_num():
    """ get random number """
    while 1:
        num = random.randint(1000, 9999)
        if len(set(list(str(num)))) is 4:
            return num


def guess_num(num):
    """guess number's game """
    num = list(str(num))
    while 1:
        right, error = 0, 0
        guess = input("please guess this num :")
        if list(guess) == num:
            return "success ! it's right ! "
        for index, param in zip(num, list(guess)):
            if index == param:
                right += 1
            if param in num and param is not index:
                error += 1
        print("{0}A{1}B".format(right, error))


if __name__ == '__main__':
    NUM = new_num()
    print(NUM)
    print(guess_num(NUM))
