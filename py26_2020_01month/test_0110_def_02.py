#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/1/10 16:07
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0110_def_02.py
# @Software  :PyCharm
# ----------------------------------
# 第一题：现有数据如下
print("""# 第一题：现有数据如下
users_title = ["name", "age", "gender"]
users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]
# 要求：将上述数据转换为以下格式
users = [{'name': '小明', 'age': 18, 'gender': '男'},
         {'name': '小李', 'age': 19, 'gender': '男'},
         {'name': '小美', 'age': 17, 'gender': '女'}]""")


def unpacking():
    users_title = ["name", "age", "gender"]
    users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]
    users = []
    for item in users_info:  # 遍历使用zip函数进行组合，users_info值有遍历次数改变
        users.append(dict(zip(users_title, item)))
    return users


print("答案：users = ", unpacking())

print("""第二题：请封装一个函数，按要求实现数据的格式转换
传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]""")
# 通过代码将传入参数转换为返回结果所需数据，然后返回


def info(date):
    res = []  # 初始化空列表
    for i in data:  # 遍历传值添加到初始化空列表，使用eval去除引号
        res.append(eval(i))
    print("答案：res = ", res)


data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# info(data)


print("第三题：简单题")
#  1、什么是全局变量？
print("全局变量：定义在模块里面，在模块中任何地方都可以使用。")
#  2、什么是局部变量？
print("局部变量：定义在函数里面，只能在函数里面使用。")
#  3、函数内部如何修改全局变量（声明全局变量 ）？
print("在函数声明对全局生效：使用global定义变量,在函数内进行操作会对全局生效。")
#   4、写出已经学过的所有python关键字，分别写出用途？
print("""type() :判断变量类型；for  in :遍历变量 if elif else  while ：逻辑关键字  break 跳出最近循环体 continue 结束此次流程，重新开始
and or not 逻辑操作符  def 定义函数 return  函数返回值 global ： 函数内声明全局变量  pass 函数占位符  True False :布尔值 None： 空值
is 判断变量是否一致""")
# 第四题:自己整理笔记


# -----------笔记-------------------
# 函数参数定义的几种形式
# 1、必须参数 ：定义几个就要传几个，不能多也不能少。
# 2、默认参数 ：定义时给了默认值。调用时可以不传，不传时使用默认值，传值使用传的值。
# 3、不定长参数  定义在必须参数和默认参数之后
# *args    接收元祖
# **kwargs 接收字典

# 拆包和打包
# *    对列表、元祖、字符串进行拆包
# def func(i, j, k):
#     print(i, j, k)
# list1 = [11111, 3333, 2222]
# func(*list1)
# **   对字典进行拆包 【根据key进行匹配】
# def func1(a, b):
#     print(a, b)
# dict1 = {"b": 11, "a": 22}
# func1(*dict1)

# 函数作用域
# 全局变量：定义在模块里面，在模块中任何地方都可以使用；
# 局部变量：定义在函数里面，只能在函数里面使用；

# 在函数声明对全局生效：使用global定义变量,在函数内进行操作会对全局生效。

# 内置函数
# enumerate()  获取元素下标和值，使用for遍历 返回两个值的元祖
# eval()    识别字符串中有效python表达式
# zip()  聚合打包，最短决定
# filter()  iterable  可迭代对象

