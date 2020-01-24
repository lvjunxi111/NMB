#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 9:08
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :Practice.py
# @Software  :PyCharm
# ----------------------------------


class A:
    def __init__(self,name,age,gender,course,classes):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.classes = classes

    def add(self,classes):
        self.classes.append(classes)
        print(classes)



