#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/2/6 16:55
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0203_unittest_suite.py
# @Software  :PyCharm
# ----------------------------------
import unittest
import HTMLTestRunnerNew
from py26_2020_02month.test_0203_unittest_testcases import RegisterTest
from py26_2020_02month import test_0203_unittest_testcases

# 创建测试套件
suite = unittest.TestSuite()

# 加载测试用例,使用类方法
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTest))

# 执行
# runner = unittest.TextTestRunner()
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=open("20200203_first_unittest.html","wb"),
                                          title="接口测试报告",
                                          description="2020年第一份接口测试报告",tester="LvJunXi")
runner.run(suite)


