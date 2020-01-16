#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/1/15 20:52
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0115_os_try.py
# @Software  :PyCharm
# ----------------------------------
import os,random


# 1、实现一个文件复制器函数，通过给函数传入一个路径，复制该路径下面所有的文件(目录不用复制)到当前目录，
# 要求：如果传路径不存在，不能报错
# 提示：os模块结合文件读写操作 、异常捕获


def copy_files(filepath):
    """ 传入一个路径，复制路径内文件到该目录下"""
    try:
        file_list = os.listdir(filepath)
    except FileNotFoundError:
        """当路径不存在时，友善提示"""
        print(filepath, "路径不存在，请检查输入路径重新操作！")
    else:
        for item in file_list:
            file = os.path.join(filepath, item)
            """先判断是不是文件，使用copyfile读取,再用save_file保存"""
            if os.path.isfile(file):
                with open(file, "rb") as copy_file:
                    readfile = copy_file.read()
                save_file_path = os.path.join(os.getcwd(), item)
                with open(save_file_path, "wb") as save_file:
                    save_file.write(readfile)
    finally:
        pass


path = "D:\\work"
# copy_files(path)

# 第二题2、改善上节课扩展作业的注册程序，打开文件的读取数据的时候，如果文件不存在会报错，
#         请通过try - except来捕获这个错误，进行处理，让注册程序可以继续运行。
# 定义一个文件名，用于保存注册用户信息
login_txt = "2019_01_14_login.txt"


def get_data(username):
    """第一次注册时，文件不存在直接返回False,进行注册"""
    try:
        with open(login_txt, "r", encoding="utf8") as login_file:
            """读取文件，查看用户名是否存在，存在返回 True"""
    except FileNotFoundError:
        return False
    else:
        with open(login_txt, "r", encoding="utf8") as login_file:
            for name in login_file.readlines():
                user = eval(name.rstrip(";\n"))
                if user.get('username') == username:
                    return True
    finally:
        pass


def create_username(username, password):
    """向2019_01_14_login.文件追加注册用户信息"""
    with open(login_txt, "a", encoding="utf8") as write_file:
        write_file.write(str({"username": username, "password": password}) + ";\n")


def login():
    """注册入口"""
    while True:
        username = input("请输入用户名(输入Q/q退出程序！)：")
        if username.upper() != "Q":
            password1 = input("请输入密码：")
            password2 = input("请再次确认密码！")

            """调用get_data()查看用户是否注册，未注册且密码一致时调用create_username()"""
            if str(get_data(username)) == "True":
                print("该用户已注册！！！")
            else:
                if password1 == password2:
                    print("注册中。。。")
                    create_username(username, password1)
                    print("注册完成！！！")
                else:
                    print("输入的密码不一致！！！")
        else:
            print("退出程序！！！")
            break


# login()  # 调用注册内容

# 第三题3、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题。


def a_came_about_love():
    print("---剪刀石头布游戏游戏说明----\n"
          "数字1代表：石头，数字2代表：剪刀，数字3代表：布。输入4退出游戏！！！\n"
          "石头赢剪刀，剪刀赢布，布赢石头")
    while True:
        random1 = random.randint(1, 3)
        list5 = ["空", "石头", "剪刀", "布", "退出"]
        try:
            number5 = int(input("出招吧！！"))
        except ValueError:
            print("仔细点，您只能输入1-4之间的整数！")
        else:
            if 0 < number5 < 5:
                if int(number5) == 4:
                    print("客官常来啊，撒油娜啦！！！")
                    break
                elif int(number5) == random1:
                    print(f"机器出{list5[random1]}，你出{list5[int(number5)]}，我们打平了！")
                    continue
                elif int(number5) - random1 == 2 or int(number5) - random1 == -1:
                    print(f"机器出{list5[random1]}，你出{list5[int(number5)]}，您赢了！")
                    continue
                else:
                    print(f"机器出{list5[random1]}，你出{list5[int(number5)]}，您输了！")
                    continue
            else:
                print("仔细点，您只能输入1-4之间的整数！")
        finally:
            pass


a_came_about_love()  #三角恋
# 第四题：整理笔记
