#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/1/7 17:39
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0108_def.py
# @Software  :PyCharm
# ----------------------------------
# 函数定义 def
# 函数返回值  return
# 1、一、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）


def multiplication_table():
    print("------九九乘法表------")
    for i in range(1, 10):
        for j in range(1, i + 1):  # 左开右闭，所以结束值需要+1
            print("{}*{}={}".format(j, i, (j * i)), end='\t')
        print()  # 换行


# multiplication_table()

# 2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
def combination():
    print("------1234四个数字可以组成无重复数字3位数有------")
    list2 = []
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if a != b and b != c and a != c:  # 过滤3个数中出现重复情况
                    str2 = str(a) + str(b) + str(c)  # 多个字符使用加号拼接拼接
                    list2.append(str2)
    print("组成的数据为{}，\n 共计{}个。".format(list2,len(list2)))


# combination()


# 3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：
# 加【1】 减【2】 乘【3】 除【4】，根据不同的选择完成不同的计算 ，然后返回结果。


def calculation():
    print("------简单计算器------")
    number1 = float(input("请输入第一个数字:"))
    number2 = float(input("请输入第二个数字:"))
    calculator = int(input("根据提示输入运算符：加【1】减【2】乘【3】除【4】>>>"))

    # 判断运算符类型，并给出返回值
    if calculator == 1:
        return number1 + number2
    elif calculator == 2:
        return number1 - number2
    elif calculator == 3:
        return number1 * number2
    elif calculator == 4 and number2 == 0:
        return "0不能作为除数！"
    elif calculator == 4:
        return number1 / number2


print(calculation())

# 4、实现一个注册的流程的函数，调用函数就执行下面要求功能
# 基本要求：
# 1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
# 2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。​
# 3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。


def register():
    register_dict = {}
    while True:
        username = input("请输入用户名(输入Q/q退出程序！)：")
        if username.upper() != "Q":
            password1 = input("请输入密码：")
            password2 = input("请再次确认密码！")
            if username not in register_dict.keys():  # 判断用户名是否存在
                if password1 == password2:  # 判断两次输入的密码是否一致
                    register_dict[username] = password1
                    print("注册成功")
                else:
                    print("两次输入密码不一致")
            else:
                print("用户名已存在")
        else:
            print("程序结束")
            break


# register()

