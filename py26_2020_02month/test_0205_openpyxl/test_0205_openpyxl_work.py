#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/2/7 15:16
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0205_openpyxl_work.py
# @Software  :PyCharm
# ----------------------------------
import openpyxl
# -------------作业-----------------
# 通过代码读取附件文件中的register这个表单的第一行和第二行数据，
# 想办法保存为一个字典：格式如下：
# {'case_id': 1, 'title': '正常注册','data': "('python1', '123456', '123456')",'expected': '{"code": 1, "msg": "注册成功"}','result': None}

# 读取cases.xlsx 文件
workbook_1 =openpyxl.load_workbook("cases.xlsx")

# 精确到具体表单
sh_reg = workbook_1["register"]

# 精确到具体行，第1/2行
data = list(sh_reg.rows)
list_1 = [i.value for i in data[0]]     # 第一行
list_2 = [i.value for i in data[1]]     # 第二行
# 使用zip函数打包数据
data_zip = dict(zip(list_1, list_2))
print(data_zip)




