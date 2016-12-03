
"""
    Python的星号表达式可以用来解决这个问题。
    比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
    如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有24个呢？这时候星号表达式就派上用场了：
"""


def avg(middle):
    """
        传入一个数组，返回这个数组的平均值
    :param middle: 一个数组
    :return: avg
    """
    avg_list = []
    [avg_list.append(i) for i in middle]
    return sum(avg_list)/len(avg_list)


def drop_first_last(grades):
    """
        求某个list中的参数的平均值
    :param grades:
    :return:
    """
    first, *middle, last = grades
    print(first, last)
    return avg(middle)


def reacord_demo():
    """
        这是一个cookbook的* 号表达式的demo
    :return:
    """
    record = ('Dave', 'dave@example.com', '777-371-1223', '754-555-1122')
    name, email, *phone = record
    print("name :", name)
    print("email :", email)
    print("phone :", phone)
