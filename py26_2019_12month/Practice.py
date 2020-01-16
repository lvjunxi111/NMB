#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 9:08
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :Practice.py
# @Software  :PyCharm
# ----------------------------------
#
import os

# 写入
# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)
# 读取
# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
#     print(numbers)
print(__file__)
os.chdir("..")
print(os.path.abspath(__file__))
a = 1
