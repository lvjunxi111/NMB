#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/27 18:53
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0103_if_else.py
# @Software  :PyCharm
# ----------------------------------
import random

# 一、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
list1 = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
print(list1, "\n要求一：去除列表中的重复元素，")
print(list(set(list1)))
print("要求二：删除 77，88，99这三个元素")
set1 = {77, 88, 99}
print(list(set(list1) - set1))

# 二、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折，
# 如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。
number = float(input("想知道价格优惠，请输入购买金额！"))
if number < 50:
    print(f"小于50元没有优惠，需支付原价:{number}")
elif number <= 100:
    print("九折优惠，原价{},现价{}".format(number, (number * 0.9)))
else:
    print("八折优惠，原价{},现价{}".format(number, (number * 0.8)))
#  三、输入一个5位整数（不需要考虑其他数据类型），判断它个位与万位相同，十位与千位相同。
# 根据判断打印出相关信息，相同打印结果：该数据符合规范，不相同打印：该数据不符合规范
str1 = input("输入一个5位整数，判断它个位与万位相同，十位与千位相同。")
if str1[0] == str1[4] and str1[1] == str1[3]:
    print("个位与万位相同，十位与千位相同")
elif str1[1] == str1[3]:
    print("十位与千位相同")
elif str1[0] == str1[4]:
    print("个位与万位相同")
# 四、利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
num1 = int(input("请输入一个数字,和随机数比大小！"))
num2 = random.randint(1, 9)
if num1 < num2:
    print(f"随机数{num2},您输入的数小于随机数")
elif num1 > num2:
    print(f"随机数{num2},您输入的数大于随机数")
else:
    print(f"随机数{num2},您输入的数大于随机数")
# 如果大于随机数，则打印印大于随机数。
# 如果小于随机数，则打印小于随机数。
# 如果相等随机数，则打印等于随机数。

# 五、实现剪刀石头布游戏，运行代码，提示用户输入出拳的数字 ：石头（1）／剪刀（2）／布（3）
# 电脑随机生成出拳数字，
# 然后比较胜负，打印游戏结果，

number5 = int(input("剪刀石头布游戏:输入出拳的数字[1=石头,2=剪刀,3=布]"))
list5 = ["空", "石头", "剪刀", "布"]
random1 = random.randint(1, 3)
if number5 == random1:
    print(f"机器出{list5[(random1)]}，你出{list5[(number5)]}，你们打平了！")
elif number5 - random1 == 2 or number5 - random1 == -1:
    print(f"机器出{list5[(random1)]}，你出{list5[(number5)]}，您赢了！")
else:
    print(f"机器出{list5[(random1)]}，你出{list5[(number5)]}，您输了！")
# 六、提示用户输入一个数（只考虑整数），判断这个数能同时被3和5整除，
number6 = int(input("请输入一个数，判断这个数能同时被3和5整除"))
if number6 % 3 == 0 and number6 % 5 == 0:
    print("这个数据我喜欢")
else:
    print("这个数据不太喜欢")
# 能整除打印 :这个数据我喜欢
# 不能整除打印：这个数据不太喜欢

# 集合：{}空集合 set1 = set()
# 集合中只能存放不可变类型数据；不可重复。
# 集合添加：add
# 集合删除：pop 、remove
# 集合： 交集 a&b  并集 a|b 差集 a-b

# if_elif_else
# 非0为true ；None 为False 空列表、字典为false
