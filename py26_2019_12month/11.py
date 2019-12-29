#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 9:08
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :11.py
# @Software  :PyCharm
# ----------------------------------
import random

def phone_number():
    for i in range(1):
        top = "130"
        for item in range(8):
            number1 = str(random.randint(0, 9))
            top += str(number1)
        print(top)


# phone_number()
