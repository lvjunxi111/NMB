#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/28 16:48
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :output.py
# @Software  :PyCharm
# ----------------------------------


def print_end():
    a = "*"
    end = ("{}\
            \n{:<5}{:<15}{:<1}{:<12}{:<7}{}{:>1}{:>13}\
            \n{:<5}{:<15}{:<3}{:<11}{:<7}{}{:>7}{:>10}\
            \n{:<5}{:<15}{:<5}{:<9}{:<7}{}{:>9}{:>8}\
            \n{:<5}{:<15}{:<7}{:<7}{:<7}{}{:>10}{:>7}\
            \n{:<5}{:<15}{:<9}{:<5}{:<7}{}{:>9}{:>8}\
            \n{:<5}{:<15}{:<11}{:<3}{:<7}{}{:>7}{:>10}\
            \n{:<5}{:<15}{:<13}{:<1}{:<7}{}{:>1}{:>13}\
            \n{}"
           .format(a * 60, \
                   "**", a * 10, a * 2, a, a * 2, a * 2, a * 4, "**", \
                   "**", a * 2, a * 2, a * 2, a * 2, a * 2, a * 3, "**", \
                   "**", a * 2, a * 2, a * 2, a * 2, a * 2, a * 3, "**", \
                   "**", a * 10, a * 2, a * 2, a * 2, a * 2, a * 3, "**", \
                   "**", a * 2, a * 2, a * 2, a * 2, a * 2, a * 3, "**", \
                   "**", a * 2, a * 2, a * 2, a * 2, a * 2, a * 3, "**", \
                   "**", a * 10, a * 2, a, a * 2, a * 2, a * 4, "**", \
                   a * 60))
    print(end)

