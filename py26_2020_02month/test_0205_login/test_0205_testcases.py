#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/2/7 11:46
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0205_testcases.py
# @Software  :PyCharm
# ----------------------------------
import unittest
from py26_2020_02month.test_0205_login.test_0205_login import login


class LoginTest(unittest.TestCase):

    def __init__(self,methodName,case_data):
        self.case_data = case_data
        super().__init__(methodName)

    def test_pass(self):
        """注册成功"""
        data = self.case_data["data"]
        # 预期结果：{"code": 1, "msg": "注册成功"}
        expect = self.case_data["expect"]
        # 实际结果
        res = login(*data)
        # 断言
        self.assertEqual(expect, res)

