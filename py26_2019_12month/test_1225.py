#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/25 22:38
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_1225.py
# @Software  :PyCharm
# ----------------------------------


import random

# 导入随机取数模块


# 1、写一段代码，运行的时候在控制台依次提示提示输入姓名，年龄、性别
name = input("名字")
sex = input("性别")
age = input("年龄")

print("************************\n名字：  {}\n性别：  {}\n年龄：  {}\n************************".format(name,sex,age))
print("************************"+"\n名字：  "+name+"\n性别：  "+sex+"\n年龄：  "+age+"\n************************")
# print("""
# ************************
# 名字：  {name}
# 性别：  {sex}
# 年龄：  {age}
# ************************
# """.format(name=name, sex=sex, age=age))

# 2、请描述一下标识符的命名规范，和有哪几种命名风格？（简单题）
# 下划线命名（变量命名使用这个风格，函数也推荐使用这个规则）
# min_number = 0
# 大驼峰命名(类命名推荐使用这个风格)
# MinNumber = 0
# 小驼峰命名(包命名和模块命名使用较多)
# minNumber = 0
# 3、现在有变量a = ‘hello’, b = ‘python18’    c = ‘!’, 通过相关操作转换成字符串：'hello python18 !'（注意点: 转换之后单词之间有空格）
a = "hello"
b = "python18"
c = "!"
print(a + " " + b + " " + c)
print(" ".join((a, b, c)))
# 4、现在有一个字符串s = 'abcdefghijk'
s = "abcdefghijk"
# 要求一：通过切片获取: defg
print(s[3:7])
# 要求二：通过切片获取：cgk
print(s[2::4])
# 要求三：通过切片获取：jhf
print(s[-2:-8:-2])
print(s[9:3:-2])

# 5、本堂课的内容终结成笔记（最好是思维导图）
# ---数值类型---
# 整数（int）
# 浮点数(float) 小数位默认显示1位小数
# 布尔值(bool)  True & False

# ---运算符---
# 算数运算符：加+ 减- 乘* 除/ 取余% 幂** 整除//
# 赋值运算符：+= -= = *= /= %=
# a +=b   等于 a = a + b

# ---比较运算符---
# 等于 ==  不等于 !=  大于等于 >=   小于等于 <=

# ---逻辑运算符---
# 或or 与and  非not

# 随机生成一个数 先导入随机取数模块import random,导入模块需要放在文件头部

random.random()  # 0到1随机取一个小数
random.randint(1, 3)  # 1到3随机取一个整数，包含1和3

# 字符串
# 字符串拼接 "拼接符".join((str1,str2))

# 切片 下标从0开始，左闭右开 step小于0反向切片
# object[start_index:end_index:step]

# 标识符命名
# 下划线命名（变量命名使用这个风格，函数也推荐使用这个规则）
min_number = 0
# 大驼峰命名(类命名推荐使用这个风格)
MinNumber = 0
# 小驼峰命名(包命名和模块命名使用较多)
minNumber = 0
