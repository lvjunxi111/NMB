#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2019/12/29 13:29
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_1230_list_dict.py
# @Software  :PyCharm
# ----------------------------------
# 一、现在有一个列表 li2=[1，2，3，4，5]，
print("第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]")
list1 = [1, 2, 3, 4, 5]
list1.insert(0, 0)
list1[4] = 66
list1.extend([11, 22, 33])
print(list1)

print("第二步：对列表进行升序排序 （从小到大）")
list1.sort(reverse=False)
print(list1)
print(" 第三步：将列表复制一份进行降序排序（从大到小）")
list2 = list1.copy()
list2.sort(reverse=True)
print(list2)

# 二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
# 将输入的信息作为添加的列表中保存，然后按照一下格式输出：
# 用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对（要求：输出的身高要求保留2位小数）
user = []
name = input("姓名？")
user.append(name)
age = int(input("年龄？"))
user.append(age)
height = round(float(input("身高？")), 2)
user.append(height)
print(f"用户的姓名为：{user[0]},年龄为：{user[1]},  身高为：{user[2]}m ")

# 三、有下面几个数据 ，
print("""t1 = ("aa",11)      t2= ("bb",22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}""")
# 要注意字典中元素的顺序（使用python3.5以下的同学不用考虑位置）
t1 = ("aa", 11)
t2 = ("bb", 22)
li1 = [("cc", 11)]
dict1 = {t1[0]: t1[1], li1[0][0]: 22, t2[0]: t2[1], }
print(dict1)
# 四、有5道题（通过字典来存储数据）： 某比赛需要获取你的个人信息，设计一个程序，
#  1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
#  2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
#  3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
#  4、平台为了保护你的隐私，需要你删除你的联系方式；
#  5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。

dict2 = {}
name = input("姓名？")
dict2["name"] = name
gender = input("性别？")
dict2["gender"] = gender
age = input("年龄？")
dict2["age"] = age
print(f"我的名字是：{dict2['name']},今年{dict2['age']}岁，性别{dict2['gender']}，喜欢敲代码！")
dict2.update({'height': '100', 'tel': '12345678910'})
print("新增两个键值对：", dict2)
dict2.pop('tel')
print("删除键值对tel:", dict2)
dict2['Skill'] = "睡觉"
print("添加一个键值对", dict2)

# 五、请指出下面那些为可变类型的数据，那些为不可变类型的数据
# 1 、 (11)
# 2 、 "111"
# 3 、 ([11,22,33])
# 4 、 {"aa":111}
print("""不可变的是:(11),"111";可变的是：{"aa":111},([11,22,33])""")
# 6、请获取下面数据中的token，和reg_name
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
# print(data.get("data").get("token_info").get("token"))
print("获取token值：", data["data"]["token_info"]["token"])
# 7、切片
# 1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("li = [1, 2, 3, 4, 5, 6, 7, 8, 9]")
print("取3，6，9:", li[2:][::3])
# 2、s = 'python java php',通过切片获取: java
s = 'python java php'
print("s = 'python java php'")
print("输出java:", s[7:11])
# print(s.split()[1])
# 3 、tu = ('a','b','c','d','e','f','g','h'),通过切片获取 ['g','b']
tu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print("tu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')")
print("获取['g','b']:", tu[-2::-1][::5])
# 8、请分别列出学过的字符串方法，列表的方法、字典的方法、元祖的方法，并指出方法的作用
item = "123"
str1 = " ".join(item)  # 拼接.前面的是拼接符
str1.replace('old','new') # 替换
list.append('item')  # 末尾添加
list.insert(1, 2)  # 指定位置添加
list.remove([1, 2])  # 尾部添加列表
list.reverse()  # 倒叙
list.sort(reverse=True)  # 大小顺序排序
dict["name"] = "LvJunXi"  # 添加键值对，key存在修改value
dict.update({"age": 12, "gender": 1})  # 添加多个键值对【合并】
dictMerged2 = dict( dict1, **dict2 ) # 合并dist1 和 dist2
dict.popitem()  # 默认删除最后一个键值对
dict.pop('key')  # 删除指定键值对
tuple #元祖不能修改&删除单个值&添加    可以相加
# 9、总结笔记

# --------------笔记-----------------
list1 = []  # 列表
# list.append(a)   加在尾部
# list.insert(a,b) a是位置，b是添加的数据
# list.extend(list) 在尾部添加一个list
list1.extend([1, 2, 3])
# print(list1)

# list1.remove(a)   删除指定元素，不存在报错
# list.pop(i)   根据列表下标删除
# list.clear    将列表清空，变为一个空列表
