#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 9:08
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :Practice.py
# @Software  :PyCharm
# ----------------------------------


def func_04(n):
    # 递归解决猴子摘桃子总数问题，每天吃掉一半多一个。
    if n == 10:
        return 1
    else:
        return func_04(n + 1) * 2 + 2



