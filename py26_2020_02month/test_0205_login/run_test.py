#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/2/7 13:06
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :run_test.py
# @Software  :PyCharm
# ----------------------------------
import unittest

from HTMLTestRunnerNew import HTMLTestRunner
from py26_2020_02month.test_0205_login.test_0205_testcases import LoginTest

cases = [{"expect": {"code": 1, "msg": "注册成功"}, "data": ("lvjunxi", "123456", "123456")},
         {"expect": {"code": 0, "msg": "所有参数不能为空"}, "data": (None, "123456", "123456")},
         {"expect": {"code": 0, "msg": "所有参数不能为空"}, "data": ("lvjunxi1", None, None)},
         {"expect": {"code": 0, "msg": "两次密码不一致"}, "data": ("lvjunxi2", "123456", "12345666")},
         {"expect": {"code": 0, "msg": "该账户已存在"}, "data": ("python26", "123456", "123456")},
         {"expect": {"code": 0, "msg": "账号和密码必须在6-18位之间"}, "data": ("lvjunxi3", "12345", "12345")}]
# case_data_1 = {"expect":{"code": 1, "msg": "注册成功"},"data":("lvjunxi", "123456", "123456")}

# 创建测试套件
suite = unittest.TestSuite()

# 通过遍历测试用例数据
for case in cases:
    # 创建一个测试用例(一个测试用例对象)
    cases = LoginTest("test_pass", case)
    # 加载到测试套件中
    suite.addTest(cases)

# 创建测试运行程序,
# 执行
# runner = unittest.TextTestRunner()
runner = HTMLTestRunner(stream=open("report_0205.html", "wb")
                        , title="接口测试报告0205"
                        , description="测试报告"
                        , tester="LvJunXi")
runner.run(suite)
