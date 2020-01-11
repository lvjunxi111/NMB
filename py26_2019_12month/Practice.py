#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 9:08
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :Practice.py
# @Software  :PyCharm
# ----------------------------------
#
def info(*args):
    res = [] # 初始化空列表
    for i in args[0]: # 遍历传值添加到初始化空列表，使用eval去除引号
        res.append(eval(str(i)))
    print("res = ", res)


data = ["{'a':11,'b':2}", "[11,22,33,44]"]
info(data)




