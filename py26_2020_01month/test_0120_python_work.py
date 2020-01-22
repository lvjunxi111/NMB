# #!/usr/bin/python3
# # -*-coding:utf-8-*-
# # @time      :2020/1/21 9:14
# # @Author    :LvJunXi
# # @Mail      :18912945952@163.com
# # @File      :test_0120_python_work.py
# # @Software  :PyCharm
# # ----------------------------------
# --------------------一、填空题----------------------------
# 1、Python3.x默认使用的编码是(uft-8)。
# 2、在循环体中使用(break)可以跳出循环体。
# 3、在循环体中可以使用(continue)跳过本次循环后面的代码，重新开始下一次循环。
# 4、如果希望循环是无限的，我们可以通过设置条件表达式永远为(True)来实现无限循环。
# 5、函数可以有多个参数，参数之间使用(,)分隔
# 5、使用(return)可以返回函数值并退出函数。

# --------------------二、判断题----------------------------
# 1、Python使用符号  # 表示单行注释。（√）
# 2、标识符可以以数字开头。（×）
# 3、type()方法可以查看变量的数据类型。（√）
# 4、Python中标识符不区分大小写。（×）
# 5、Python中的标识符不能使用关键字。（√）
# 6、函数的名称可以随意命名。（×）
# 7、不带return的函数代表返回None。（√）
# 8、函数定义完成后，系统会自动执行其内部的功能。（×）
# 9、在使用异常时必须先导入exceptions模块。（×）
# 10、一个try语句只能对应一个except子句。（×）
# 11、所有的except子句一定在else和ﬁnally的前面。（√）
# 12、类方法的第一个参数为self(√)
# 13、对象不能调用类方法 （×）
# --------------------三、选择题----------------------------
# 1.下列选项中，（A,B,C）的布尔值不是Flase。
# A.None    B.0     C.()    D.1
# 2.下列标识符中，合法的是（A,D）
# A.helloWorld  B.2ndObj    C.hello#world   D._helloworld
# 3.字符串'Hi,Andy'中，字符'A'对应的下标位置为（C）。
# A.1   B.2     C.3     D.4
# 4.下列方法中，用于向文件中写出内容的是（B）。
# A.open    B.write     C.close     D.read
# 5.当try语句中没有任何错误信息时，一定不会执行（D）语句。
# A.try     B.else      C.ﬁnally     D.except
# 三、编程题
# 1、 用户登陆程序需求:
# 1.输入用户名和密码;
# 2.判断用户名和密码是否正确? (name='python', passwd='lemonban')
# 3.为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 提示错误次数过多，账号已被冻结,;


def login():
    """登录验证程序，超过三次提示错误次数过多，账号已被冻结"""
    number = 3
    while number >= 0:
        if number == 0:
            print("错误次数过多，账号已被冻结,明日再试！")
            break
        number -= 1
        user_dict = {"name": "python", "password": "lemonban"}
        user = input("请输入用户名！")
        password = input("请输入密码！")
        if user_dict.get("name") != user or user_dict.get("password") != password:
            print("用户名或密码输入错误！")
        else:
            print("登录成功，欢迎回来{}！".format(user))
            break


# login()  # 调用登录函数

# 2、给定一个句子（只包含字母和空格）， 将句子中的单词位置反转， 比如： “hello xiao mi” > “mi xiao hello”

def inversion(str_1="hello xiao mi"):
    """输入一个句子，根据空格倒序输出"""
    str_1.split().reverse()
    return str_1


# input_str = input("请输入由空格拼接的语句！！！")
# print(inversion(input_str))

# 3、运行程序，提示用户依次输入三个整数x, y, z，请把这三个数由小到大输出。

def grade_down():
    """用户依次输入三个整数x, y, z，请把这三个数由小到大输出"""
    try:
        number_1 = int(input("请输入第一个数字！"))
        number_2 = int(input("请输入第二个数字！"))
        number_3 = int(input("请输入第三个数字！"))
    except ValueError as error:
        print("请输入整数！！！")
    else:
        number_list = [number_1, number_2, number_3]
        number_list.sort(reverse=True)
        for item in number_list:
            print(item)
    finally:
        pass


# grade_down()  # 调用函数
# 4、编写一个程序，使用for循环输出0 - 100之间的偶数
def even_num():
    """计算0到100偶数和，思路：对2趋于等于0为偶数，遍历100内偶数相加"""
    num = 0
    for number in range(101):
        if number % 2 == 0:
            num += number
    return num


# print(even_num())     # 调用求100内偶数和函数
# 5、打开一个文本文件，读取其内容，把其中的大写字母修改为小写字母，再写入文件覆盖原内容


def toggle_case(file):
    """读取文件内容并将字母转换为小写,再将转换后信息存入原文件中"""
    with open(file, 'r', encoding='utf8') as copy_file:
        file_data = copy_file.read()
        file_data = str(file_data).lower()
    with open(file, 'w', encoding='utf8') as info_file:
        info_file.write(file_data)


# toggle_case("file.txt")

# 6、现在有一个字符串s = 'asdf2273788hh90999', 请写一段代码来删除字符串中的重复元素，最后转换为列表保存。

def distinct(string):
    """将字符串去重后，转变为列表返回"""
    return list(set(string))


str_6 = "asdf2273788hh90999"


# print(distinct(str_6))
# 7、小明有100块钱 ，需要买100本书（钱要刚好花完），a类数5元一本，b类书3元一本，c类书1元2本。请计算小明有多少种购买的方式？
def pay_book():
    book_a = 5
    book_b = 3
    book_c = 0.5
    money = 100
    number = 100
    sum = 0
    for a in range(int(money / book_a)):
        for b in range(int(money / book_b)):
            for c in range(int(money / book_c)):
                if a + b + c == number and a * book_a + b * book_b + c * book_c == money:
                    sum += 1
    return "有{}种购买方式。".format(sum)


# print(pay_book())   # 调用函数

# 8、题目：小明买了一对刚出生的兔子，兔子从出生后第3个月起每个月都生一对兔子，
# 生的这对小兔子长到第三个月也开始生兔子（每个月生一对兔子），假如兔子都不死，问10个月后小明的兔子为多少对？
# （思b 路提示：重点在分析出兔子增长的规律，分析出规则之后通过for循环即可实现）？
def num(number):
    """兔子数量规律[1, 1, 2, 3, 5, 8, 13, 21],没整明白，百度搜的【small, big = big, small + big】"""
    small = 0
    big = 1
    for item in range(number - 1):
        small, big = big, small + big
    print("{}月后，兔子总数为{}对。".format(number, big))


# num(10)  # 调用函数

# 9、请封装一个函数，来实现要求的数据格式转换功能（思路提示：for循环和zip函数）：
# # 数据转换有一组用例数据如下：
# cases = [['case_id', 'case_title', 'url', 'data', 'excepted'],
#     [1, '用例1', 'www.baudi.com', '001', 'ok'],
#     [2, '用例2', 'www.baudi.com', '002', 'ok'],
#     [3, '用例3', 'www.baudi.com', '002', 'ok'],
#     [4, '用例4', 'www.baudi.com', '002', 'ok'],
#     [5, '用例5', 'www.baudi.com', '002', 'ok'],]
# # 需要转换为以下格式：
# cases02 = [{'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#            {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#            {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#            {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#            {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}]


def test_zip(cases):
    """按照给定格式使用zip打包函数转换为字典集列表"""
    list_9 = []
    for zip_val in range(1, len(cases_1)):
        case = dict(zip(cases_1[0], cases_1[zip_val]))
        list_9.append(case)
    print(list_9)


cases_1 = [['case_id', 'case_title', 'url', 'data', 'excepted'],
           [1, '用例1', 'www.baudi.com', '001', 'ok'],
           [2, '用例2', 'www.baudi.com', '002', 'ok'],
           [3, '用例3', 'www.baudi.com', '002', 'ok'],
           [4, '用例4', 'www.baudi.com', '002', 'ok'],
           [5, '用例5', 'www.baudi.com', '002', 'ok'], ]


# test_zip(cases_1) # 调用函数

# 10、题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10 %； 1
# 利润高于10万元，低于20万元时，低于10万元的部分按10 % 提成，高于10万元的部分，可提成7.5 %； 0.75
# 20万到40万之间时，高于20万元的部分，可提成5 %；.05
# 40万到60万之间时，高于40万元的部分，可提成3 %；
# 60万到100万之间时，高于60万元的部分，可提成1.5 %;
# 高于100万元时，超过100万元的部分按1 % 提成，从键盘输入当月利润I，求应发放奖金总数？


def bonus(number_10):
    # 10万内奖金金额计算
    if number_10 < 0:
        return "最好填写大于0的数！！"
    elif number_10 <= 10:
        return "奖金可发{:.2f}万".format(number_10 * 0.1)
    # 20万内奖金金额计算
    elif number_10 <= 20:
        return "奖金可发{:.2f}万".format(1 + (number_10 - 10) * 0.075)
    # 40万内奖金金额计算
    elif number_10 <= 40:
        return "奖金可发{:.2f}万".format(1.75 + (number_10 - 20) * 0.05)
    # 60万内奖金金额计算
    elif number_10 <= 60:
        return "奖金可发{:.2f}万".format(2.75 + (number_10 - 40) * 0.03)
    # 100万内奖金金额计算
    elif number_10 <= 100:
        return "奖金可发{:.2f}万".format(3.35 + (number_10 - 60) * 0.015)
    # 超过100万奖金金额计算
    elif number_10 > 100:
        return "奖金可发{:.2f}万".format(3.95 + (number_10 - 100) * 0.01)


# print(bonus(100))  # 调用计算奖金金额

# 11、编写一个自动售货机，运行功能如下:
# 1、请按下面提示，选择购买的商品
# 1).可乐 2.5元    2).雪碧2.5元   3).哇哈哈3元    4).红牛6元     5).脉动4元     6).果粒橙3.5元
# 2、提示用户投币（支持1元，5元，10元）
# 用户输入投币金额，
# 用户投币金额不够商品价格，继续提示投币，
# 当投币超过商品价格，则返回商品和找零，然后结束程序

def invest_money(sum_money=0):
    """投币方法，默认金额为0"""
    while True:
        list_rmb = ['1', '5', '10']

        # 输入0退出投币方法，返回投入金额；符合规范金额相加。
        money = input("可以投币，已投{}元，结束投币请按[0]！".format(sum_money))
        if money == "0":
            return sum_money
        elif money in list_rmb:
            sum_money += int(money)
        else:
            pass


def choose_drink():
    """购买产品方法"""
    print("欢迎使用自动售货机，只能使用1元、5元、10元！\n"
          "1).可乐 2.5元    2).雪碧2.5元   3).哇哈哈3元    4).红牛6元     5).脉动4元     6).果粒橙3.5元")

    # 开始调用投币方法，获取投入金额
    sum_money = invest_money()
    while True:

        # 定义一个列表和字典，根据输入获取对饮产品和单价
        list_drinks = [0, "可乐", "雪碧", "娃哈哈", "红牛", "脉动", "果粒橙"]
        dict_drinks = {"可乐": 2.5, "雪碧": 2.5, "娃哈哈": 3, "红牛": 6, "脉动": 4, "果粒橙": 3.5}
        try:
            drink = int(input("余额{}，请选择购买的饮料,退钱请按[0],投币请按[9]".format(sum_money)))
        except ValueError as error:
            print("您的输入有误，请重新输入！！！")
        else:

            # 输入0退还金额，购物结束！
            if drink == 0:
                print("退出金额{}元。\n欢迎再次使用！祝您天天好心情！".format(sum_money))
                break

            # 输入9调用投币方法继续投币！
            elif drink == 9:
                sum_money = invest_money(sum_money=sum_money)

            # 符合规定产品范围，金额剩余可继续操作，无则程序结束
            elif 1 <= drink <= 6:
                if sum_money - dict_drinks[list_drinks[drink]] > 0:
                    sum_money -= dict_drinks[list_drinks[drink]]
                    print("您选择了{}，花费{}元，余额{}元。".format(list_drinks[drink], dict_drinks[list_drinks[drink]], sum_money))
                elif sum_money - dict_drinks[list_drinks[drink]] == 0:
                    print("您选择了{}，花费{}元，余额{}元。\n不要忘记你的{},欢迎再次使用".
                          format(list_drinks[drink], dict_drinks[list_drinks[drink]], 0, list_drinks[drink]))
                    break
                else:
                    print("{}需要{}元，剩余金额{}元，余额不足！投币请按[9]。"
                          .format(list_drinks[drink], dict_drinks[list_drinks[drink]], sum_money))
            else:
                print("您的输入有误，请重新输入！！！")


# choose_drink()  # 调用自动售货机方法

# 12、封装一个老师类
# 属性：姓名、年龄、性别、授课科目、授课班级（list类型，可以保存多个班级）
# 方法： 添加授课班级 、 打印老师的信息
class Teacher:
    def __init__(self, name, age, gender, course, *args):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.args = args

    # 添加授课班级【不太清楚要做什么】
    def insert_class(self):
        list_class = []
        list_class.extend(self.args)
        print(list_class)

    # 打印老师的信息
    def print_information(self):
        print("打印教师信息>>姓名：{}，年龄：{}，性别：{}，科目：{}，班级：{}。"
              .format(self.name, self.age, self.gender, self.course, list(self.args)))


# teacher = Teacher("吕军喜", 18, "男", "语文", "1班", "2班", "3班")
# teacher.insert_class()
# teacher.print_information()

# 13、类和继承
# 要求一：定义一个游戏英雄类（Hero）
# 特征（属性）：名字（name）、血量（HP）
# 行为（方法）：技能1：移动
# 要求二：定义一个战士类（继承英雄类）
# 除了上面英雄类的属性之外，还多了一个属性：攻击力（attack）和一个方法：技能2（普通攻击）
# 要求三：定义一个法师类（继承英雄类）
# 除了上面英雄类的属性之外，还多了一个属性：法力值（MP）和一个方法：技能2（法术攻击）


class Hero:
    """定义一个英雄类"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @staticmethod
    def walk():
        print("拥有walk技能！")


class Warrior(Hero):
    """定义一个战士类,继承Hero类"""

    # 定义子类属性，继承父类，添加子类特有属性attack
    def __init__(self, name, hp, attack):
        super().__init__(name, hp)
        self.attack = attack

    @classmethod
    def common_attack(cls):
        print("拥有common_attack技能！")


class Master(Hero):
    """定义一个法师类,继承Hero类"""

    def __init__(self, name, hp, master):
        super().__init__(name, hp)
        self.master = master

    @staticmethod
    def master_attack():
        print("拥有master_attack技能！")


""" 一个父类[Hero] 两个子类[Master、Warrior]
父类Hero      work为静态方法
子类Master    master_attack为静态方法
子类Warrior   common_attack为类方法

静态方法没有self参数
类  方法默认参数cls

静态方法调用：类.方法 / 对象.方法
类  方法调用：类.方法 / 对象.方法     
"""
