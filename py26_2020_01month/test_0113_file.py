#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/1/13 9:32
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0113_file.py.py
# @Software  :PyCharm
# ----------------------------------
# 第一题：当前有一个txt文件，内容如下：
# 数据aaa
# 数据bbb
# 数据ccc
# 数据ddd
# 要求：请将数据读取出来，保存为以下格式
# {'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}
# 提示：可能会用到内置函数enumerate，注意点：读取出来的数据如果有换行符'\n'，要想办法去掉。


def change_dict_data():
    with open("2019_01_14_file01.txt", "r", encoding="utf8") as file01:
        """初始化一个列表和字典"""
        data_list = []
        data_dict = {}

        """遍历将文件中信息存到列表中"""
        for item in file01:
            data_list.append(item.rstrip())

            """使用enumerate函数遍历元素，生成升序key"""
            for data_key, data_value in enumerate(data_list):
                data_dict["data" + str(data_key)] = data_value
        print("第一题")
        print(data_dict)


# change_dict_data()  # 调用函数


# 第二题：当前有一个case.txt文件，里面中存储了很多用例数据: 如下，每一行数据就是一条用例数据，
# 文件中数据（可以先直接复制到文件中）
# ur1:www.baidu.com,mobilephone:13760246701,pwd:123456
# ur2:www.baidu.com,mobilephone:15678934551,pwd:234555
# ur3:www.baidu.com,mobilephone:15678934551,pwd:234555
# ur4:www.baidu.com,mobilephone:15678934551,pwd:234555
# ur5:www.baidu.com,mobilephone:15678934551,pwd:234555
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
# [{'ur1': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
# {'ur2': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
# {'ur3': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
# {'ur4': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
# {'ur5': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}]
# 提示：可以分析读取出来的每一行字符串中的内容，然后使用的字符串分割方法进行分割，想办法组装成字典。
# 注意点：数据中如果有换行符'\n'，要想办法去掉。

def change_list_data():
    with open("2019_01_14_file02.txt", "r", encoding="utf8") as file02:

        """初始化一个列表，一行一行遍历文件中数据"""
        data_list = []
        for item2 in file02.readlines():

            """初始化一个字典，使用rstrip()去除换行符；使用split()拆分数据，需要分离两次，最后新增到字典中后添加到列表里"""
            data_dict1 = {}
            for a in item2.rstrip().split(','):
                data_dict1[a.split(':')[0]] = a.split(':')[1]
            data_list.append(data_dict1)
        print("第二题")
        print(data_list)


# change_list_data()  # 调用函数

# 第三题：总结笔记
# read(size):读取文件前size个字节数据，无则读取所有数据
# readline():每次读取文件1行内容，读取时占用内存小，比较适合大文件
# readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存[遍历]
# linecache()有特殊需求还可以用linecache模块，比如你要输出某个文件的第n行：/
# 输出第2行  text = linecache.getline('a.txt',2)

# 第四题：扩展题（不要求提交，有时间的同学可以去思考一下）：
# 之前作业写了一个注册的功能，再之前的功能上进行升级，
# 要求：把所有注册成功的用户数据放到文件中进行保存，确保下一次运行代码的时候，上一次运行注册的账号数据还在。

# 注册用户信息保存格式：{'username':'lvjunxi','password':'123456'};
# 查看用户数据判断新增用户是否注册
def get_data(username):
    username = username
    # password = password
    with open("2019_01_14_login.txt","r",encoding="utf8") as login_file:
        """读取文件，查看用户名是否存在，存在返回 True"""
        for name in login_file.readlines():
            # print(name)
            a = eval(name.rstrip(";\n"))
            if a.get('username') == username:
                return True

# 向2019_01_14_login.文件追加注册用户信息
def create_username(username,password):
    username = username
    password = password
    with open("2019_01_14_login.txt","a",encoding="utf8") as write_file:
        write_file.write(str({"username":username,"password":password})+";\n")

# 注册入口
def login():
    while True:
        username = input("请输入用户名(输入Q/q退出程序！)：")
        if username.upper() != "Q":
            password1 = input("请输入密码：")
            password2 = input("请再次确认密码！")

            """调用get_data()查看用户是否注册，未注册且密码一致时调用create_username()"""
            if str(get_data(username))=="True":
                print("该用户已注册！！！")
            else:
                if password1 == password2:
                    print("注册中。。。")
                    create_username(username, password1)
                    print("注册完成！！！")
                else:
                    print("输入的密码不一致！！！")


# login()  #调用注册内容

