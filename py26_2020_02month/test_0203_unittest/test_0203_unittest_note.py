#!/usr/bin/python3
# -*-coding:utf-8-*-
# @time      :2020/2/6 13:37
# @Author    :LvJunXi
# @Mail      :18912945952@163.com
# @File      :test_0203_unittest_note.py
# @Software  :PyCharm
# ----------------------------------
import unittest
from HTMLTestRunnerNew import HTMLTestRunner

def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if username is not None and password is not None:
        if username == 'python26' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}

# 第一条用例
# 入参 账号：python26  密码lemonban
# 预期结果：
expect = {"code": 0, "msg": "登录成功"}
# 实际结果
result = login_check('python26','lemonban')
result1 = login_check(None,None)


# 断言 assert
# 断言条件通过，不会有任何返回，直接执行下一行代码；
# 断言不通过，会报错（断言异常）
# assert expect == result

"""测试用例类：继承于unittest.TestCase就是测试用例类"""


class LoginTest(unittest.TestCase):

    def test_login_pass(self):
        """正常登录"""
        data = ("python26","lemonban")  # 入参
        expected = {"code": 0, "msg": "登录成功"} # 预期
        res_1 = login_check(*data)  # 实际结果（传入参数，调用功能。）
        self.assertEqual(expect, res_1) # 断言，比较预期和实际

    def test_login_name_none(self):
        """账号为空"""
        data = (None, None)  # 入参
        expected = {"code": 1, "msg": "所有的参数不能为空"} # 预期
        res_1 = login_check(*data)  # 实际结果（传入参数，调用功能。）
        self.assertEqual(expected, res_1) # 断言，比较预期和实际

#
    def setUp(self):
        pass    # 该方法在每条测试用例执行之前会调用
    def tearDown(self):
        pass    # 该方法在每条测试用例执行之后会调用
    @classmethod
    def setUpClass(cls):
        pass    # 该方法在测试类中的测试用例执行之前会调用
    @classmethod
    def tearDownClass(cls):
        pass    # 该方法在测试类中的测试用例执行之后会调用

# 测试套件：使用unittest.TestSuite这个类创建出来得对象就是测试套件。
# 测试运行程序：使用unittest.TextTestRunner创建对象就是测试运行程序。
# 测试用例加载对象：unittest.TestLoader。

# 第一步，创建测试套件
suite = unittest.TestSuite()

# 第二步，测试用例添加到套件中。
#   方法1：添加1条  【test_login_pass 为1个例方法】
# case_1 = LoginTest("test_login_pass")
# suite.addTest(case_1)

#   方法2：通过测试用例类加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTest))

#   方法3：通过用例模块加载测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(文件名))

# 方法4：通过制定路径加载测试用例（默认加载以test开头模块中测试用例）pattern  参数匹配加载模块
# loader = unittest.TestLoader()
# suite.addTest(loader.discover("模块路径"))

# unittest 中默认加载器
# unittest.defaultTestLoader.loadTestsFromTestCase()

#第三步，执行测试用例  ,title=None,description=None,tester=None
# runner = unittest.TextTestRunner()
runner = HTMLTestRunner(stream=open("report.html","wb"))
runner.run(suite)



