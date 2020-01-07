#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/1/6 17:58
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0106_debug.py
# @Software  :PyCharm
# ----------------------------------
import random

# 1、 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
sum1 = 0
height = 100
for item in range(1, 11):
    sum1 = sum1 + height * 2
    height = height / 2
    if item == 10:
        print(f"第一题：第{item}天，共经过{sum1 - 100}m。")

# 2、猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半  在加一个。到第10天早上想再吃时，见只剩下一个桃子了。
# 请通过一段通过代码来计算第一天摘了多少个桃子？
sum2 = 1
for day in range(9, 0, -1):
    sum2 = (sum2 + 1) * 2
    if day == 1:
        print("第二题：第{}天，摘了桃子{}个。".format(day, sum2))

# 3、使用循环和条件语对剪刀石头布游戏进行升级，提示用户输入要出的拳 ：
# 石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示 用户胜、负还是平局，打印结果，一轮游戏完了之后，重新回到用户输入的步骤，直到用户输入4退出游戏，如下图所示：
while True:
    random1 = random.randint(1, 3)
    list5 = ["空", "石头", "剪刀", "布", "退出"]
    str1 = ["1", "2", "3", "4"]
    number5 = input("剪刀石头布游戏:输入出拳的数字[1=石头,2=剪刀,3=布]，输入4退出游戏！！！")
    if number5 in str1:
        if int(number5) == 4:
            print("游戏结束！")
            break
        elif int(number5) == random1:
            print(f"机器出{list5[random1]}，你出{list5[int(number5)]}，你们打平了！")
            continue
        elif int(number5) - random1 == 2 or int(number5) - random1 == -1:
            print(f"机器出{list5[random1]}，你出{list5[int(number5)]}，您赢了！")
            continue
        else:
            print(f"机器出{list5[random1]}，你出{list5[int(number5)]}，您输了！")
            continue
    else:
        print("请按规则输入！")

# ----------笔记----------------
# break 跳出循环体
# continue 跳出本次循环
# for item in range(start,stop,step):   start 起始位，stop 终止位，step 步长
# dict ={"name":"lvjunxi","age":15}
# for item in dict.items():   # 返回的是是元祖items 有两个值
#     print(item)
