#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/2/6 17:23
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0203_unittest_testcases.py
# @Software  :PyCharm
# ----------------------------------
import unittest

from py26_2020_02month.test_0203_unittest_register import register


class RegisterTest(unittest.TestCase):


    def test_pass(self):
        """注册成功"""
        data = ("lvjunxi", "123456", "123456")
        # 预期结果：{"code": 1, "msg": "注册成功"}
        expect = {"code": 1, "msg": "注册成功"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)

    def test_name_None(self):
        """用户名不能为空"""
        data = (None, "123456", "123456")
        # 预期结果：{"code": 0, "msg": "所有参数不能为空"}
        expect = {"code": 0, "msg": "所有参数不能为空"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)

    def test_pwd_None(self):
        """用户名不能为空"""
        data = ("lvjunxi", None, None)
        # 预期结果：{"code": 0, "msg": "所有参数不能为空"}
        expect = {"code": 0, "msg": "所有参数不能为空"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)

    def test_pwd_different(self):
        """两次密码不一致"""
        data = ("lvjunxi", "123456", "12345666")
        # 预期结果：{"code": 0, "msg": "两次密码不一致"}
        expect = {"code": 0, "msg": "两次密码不一致"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)

    def test_registered(self):
        """用户名已存在"""
        data = ("python26", "123456", "123456")
        # 预期结果：{"code": 0, "msg": "该账户已存在"}
        expect = {"code": 0, "msg": "该账户已存在"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)

    def test_pwd_lass_6(self):
        """密码小于6位"""
        data = ("lvjunxi", "12345", "12345")
        # 预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
        expect = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)

    def test_pwd_greater_18(self):
        """密码大于18位"""
        data = ("lvjunxi", "1234567891234567890", "1234567891234567890")
        # 预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
        expect = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 实际结果
        res = register(*data)
        # 断言
        self.assertEqual(expect, res)
