#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 9:08
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :Practice.py
# @Software  :PyCharm
# ----------------------------------
# 少时诵诗书所所所所所所所所所


from decimal import Decimal
a = 12.3455
a1 = Decimal(a).quantize(Decimal("0.00"))
print(a1)

