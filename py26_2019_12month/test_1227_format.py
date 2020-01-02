#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/27 20:48
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_1227_format.py
# @Software  :PyCharm

# 使用*打印END字样
# from py26_2019_12month.output import print_end
import random


# ------------------作业第一题------------------
# 1、用户输入一个数值，请使用比较运算符确认用户输入的是否为偶数？是偶数输出True,不是输出False
# （提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再做判段）


def digital_verification():
    number = 3
    while number > 0:
        str1 = input("第一题：请输入一个正整数！偶数返回True,奇数返回False,您有{}次机会\n在这里输入>>>".format(number))
        if not str1.isdigit():  # 判断输入字符是否全为数字
            print("您输没有输入一个正整数！")
        else:
            print(int(str1) % 2 == 0)
            break
        number -= 1
    print("-----体验结束！-----")


# digital_verification()

# ------------------作业第二题------------------
# 2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
# 待优化使用try： except  Exception

def payment_amount():
    number = 3
    while number > 0:
        try:
            # 异常处理price1 = round(float(price),2)
            # 判断输入的值是否可以转换成数值型，暂不区分正负数
            price = input("第二题：请输入橘子单价,告诉你支付金额！！您有{}次机会\n在这里输入>>>".format(number))
            price1 = round(float(price), 2) # 输入的字符不能转换成数值报错
            number1 = random.random()
            number2 = random.randint(5, 9)
            number3 = round(number1 + number2, 2)
            if price1 > 0:
                print("单价：{price1}，重量{number3:.2f},支付金额[计算到分]：${money:.2f}"
                      .format(price1=price1, number3=number3,
                              money=(number3 * price1)))
                break
            else:
                print("我们今天没有赠送和补贴！")
                continue
        except Exception:
            print("您输入的有误！")
        finally:
            number -= 1

    print("-----体验结束！-----")


# payment_amount()


# ------------------作业第三题------------------
# 3、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码。


def phone_number():
    for i in range(1):
        top = "130"
        for item in range(8):
            number1 = str(random.randint(0, 9))
            top += str(number1)
        print(f"第三题：随机产生一个130开头手机号码：{top}")


def phone_number1():
    top = ["130"]
    for item in range(8):
        number1 = str(random.randint(0, 9))
        top.append(number1)
    return "".join(top)


# for item in range(33):
#     print(phone_number1())


# phone_number()

# ------------------作业第四题------------------
# 4、现有字符串    str1 = "PHP is the best programming language in the world! "
# 要求一：将给定字符串的PHP替换为Python
str1 = "PHP is the best programming language in the world! "
str2 = str1.replace("PHP", "Python")
# print(str2)
# 要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
str3 = str2.split(" ")


# print(str3)

# ------------------作业第五题------------------
# 5、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周X”（要求：使用上课学过的知识点来做）


def week():
    number = 3
    list1 = ["周一", "周二", "周三", "周四", "周五", "周六", "周日", ]
    list2 = ["1", "2", "3", "4", "5", "6", "7"]
    while number > 0:
        str5 = input("第五题：请输入1-7之间的数字,告诉你大写周几！！您有{}次机会\n在这里输入>>>".format(number))
        if str5 not in list2:
            print("您的输入有误！")
        else:
            print("今天{}".format(list1[int(str5) - 1]))
            break
        number -= 1
    print("-----体验结束！-----")

# week()
# --------------整理笔记--------------

# 字符串转义

# 字符串通用方法
# find：查找指定元素第一个下标位置
# count: 查找指定元素个数
# replace:【替换】item.replace(self, old, new, count) count为替换次数，空替换所有
# split ：【分割】item.split(self, sep, maxsplit ) sep:分隔符  maxsplit：分割次数
# str1 = "123123"
# print(str1)
# print(str1.find("1"))  # 返回结果 ：0
# print(str1.count("1"))  # 返回结果 ：2
# print(str1.replace("1", "a"))  # 返回结果 ：a23a23
# print(str1.split("2"))  # 返回结果 ：['1', '31', '3']

# 字符大小写转换
# upper :转换成大写
# str2 = "ABCdec123"
# print(str2.upper())  # 返回结果：ABCDEC123
# print(str2.lower())  # 返回结果：abcdec123

# format 格式化输出
# {}占位符
# {:<10}  左对齐10个字符；{:>10}  右对齐10个字符；{:^10}  居中10个字符；
# s1 = "111{0:#>10.3f}2233".format(5)  # 用#填充
# print(s1)
# % 格式化输出
# %f :浮点数；%d :整数 %s :万能
# f/F 格式化输出
# print(f"{'可是变量'}{'可是数字'}{'可是字符串'}")

# 数据类型转化  【略】
# ===============================================
#               我的作业
# ===============================================
# # ###########第一题 判断奇数偶数
# digital_verification()
# # ##########第二题   随机取数（5-10）计算
# payment_amount()
# # #########第三题解答1 [+] 随机生成130开头号码
# phone_number()
# print("-----体验结束！-----")
# # 第三题解答2 [join 拼接]
# # num = 5 # 生成号码个数
# # for item in range(num):
# #      print(phone_number1())
# # ##########第四题 字符串替换分割练习
# print("第四题1小问题：将下面字符串的PHP替换为Python")
# print(str1) # 原字符串
# print(str2) # 替换后字符串
# print("第四题2小问题：替换以后，将字符串以空格为分割点进行分割得到一个列表")
# print(str3) # 分割 后字符串
# print("-----体验结束！-----")
# # ##########第五题 输入1-7，输出周一：周日
# week()
