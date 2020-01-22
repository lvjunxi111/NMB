#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/1/17 20:01
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0117_class_01.py
# @Software  :PyCharm

# ---------作业----------------------
# 1、类属性怎么定义？ 实例属性怎么定义？
"类属性：直接定义在类里面变量"
"实例属性：方法一：通过对象进行赋值（对象名.属性名 = 属性值），方式二：通过初始化方法__init__进行定义"
# 2、实例方法中的self代表什么？（简答）
"self 代表的是对象本身；哪个对象去调用方法，self 就代表哪个对象本身。"
# 3、类中__init__方法在什么时候会调用的？（简答）
"类去创建对象的时候，__init__方法会自动调用。"
# 4、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
# -  属性：用例编号； url地址；请求参数；请求方法；预期结果；实际结果


class TestCase:
    def __init__(self, test_number, url, request_parameters, request_method, expected_results, actual_results):
        """定义实例属性"""
        self.test_number = test_number
        self.url = url
        self.request_parameters = request_parameters
        self.request_method = request_method
        self.expected_results = expected_results
        self.actual_results = actual_results


# 5、封装一个学生类，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)
# -  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
# 方法一：计算总分；
# 方法二：计算三科平均分；
# 方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx, 性别：xxx。

class Student:
    """定义类属性"""
    identity = "student"

    def __init__(self, name, age, gender, english, mathematics, chinese):
        """定义实例属性"""
        self.name = name
        self.age = age
        self.gender = gender
        self.english = english
        self.mathematics = mathematics
        self.chinese = chinese

    def total_fraction(self):
        """ 计算语数外总分"""
        total = (self.english + self.mathematics + self.chinese)
        return "语数外总分为：{}".format(total)

    def average_fraction(self):
        """ 计算语数外平均分"""
        average = (self.english + self.mathematics + self.chinese) / 3
        return "语数外平均分为：{:.2f}".format(average)

    def print_information(self):
        """打印学生个人信息"""
        return "我的名字叫：{}，年龄：{}，性别：{}。".format(self.name, self.age, self.gender)


student_1 = Student("吕军喜", 18, "男", 11, 22, 33)
"""创建对象 student_1"""

a = student_1.total_fraction()
b = student_1.average_fraction()
c = student_1.print_information()
print(a,b,c)

"""
类用于封装属性和方法
class 类名：
    类的属性和方法
创建对象 object = class（）
对象：通过类创建出来的，拥有这个类所有特征和行为。

"类属性：直接定义在类里面变量（这个类的每个对象都有这个属性，且每个属性值都是一样的）"
"实例属性就是对象属性：这一类事物都可以有这个属性，但属性值有可能不一样。"

属性的访问和方法的调用
1、对象可不可以访问类属性；可以
2、对象可不可以访问对象属性；可以
3、对象可不可直接调用方法；可以

4、类可不可以访问类属性；可以
5、类可不可以访问对象属性；不可以
6、类可不可以直接调用方法；不可以
"""
