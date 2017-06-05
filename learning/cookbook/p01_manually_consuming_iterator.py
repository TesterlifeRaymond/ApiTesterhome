
""" 你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。
为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
"""

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    p01_manually_consuming_iterator.py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ray <liujinjia@testerlife.com>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/06 06:24:41 by ray               #+#    #+#              #
#    Updated: 2017/06/06 06:24:41 by ray              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def manual_iter():
    """ 手动读取一个文件中的所有行"""
    with open('/etc/passwd') as file:
        while 1:
            line = next(file, None)
            print(line, end='')
            if line is None:
                break

def main():
    """ main function """
    manual_iter()

if __name__ == '__main__':
    main()
