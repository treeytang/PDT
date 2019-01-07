from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.user_manage.MS_manage_page import Mobile_Station
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Mobile_Station(self.driver).user_login(username, password)

    def test_come_page(self):
        '''检查进入移动台管理页面 验证'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).come_iframe_verify()
        self.assertEqual(msg.strip(), '移动用户列表')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_show_num_verify(self):
        '''检查进入移动台管理页面对显示数量的验证'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).query_num_verify()
        self.assertEqual(msg.strip(), '700')
        picture.insert_img(self.driver, "user_pwd_true.png")


    def test_come_add_icon_verify(self):
        '''进入移动台管理页面 点击开户 进入开户界面验证'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).come_add_icon()
        self.assertEqual(msg.strip(), '移动用户--开户')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_add_icon_verify(self):
        '''进入移动台管理页面 点击开户 进入开户界面验证'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1()
        self.assertEqual(msg.strip(), '添加成功')


    def test_add_icon_verify_1(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的正确用户'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1()
        self.assertEqual(msg.strip(), '添加成功')

    def test_add_icon_verify_1_1(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 区号最小值减一：327'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_1()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_2(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 区号最大值加一：807'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_2()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_5(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 区号最大值加一：807'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_5()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_6(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 区号最大值加一：807'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_6()
        self.assertEqual(msg, True)


    def test_add_icon_verify_2(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个已注册的正确用户'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_2()
        self.assertEqual(msg, True)


    def test_add_icon_verify_3(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的正确用户 实名制信息相关选择(边界值 全选第一个)'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_3()
        self.assertEqual(msg, ['海格恒通', '女', '交警', '二级警员'])

    def test_add_icon_verify_4(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个已注册的正确用户 实名制信息相关选择(边界值 全选最后一个个)'''
        self.user_login(username="thy", password="admin")
        msg = Mobile_Station(self.driver).add_icon_4()
        self.assertEqual(msg, ['科立讯', '男', '巡警', '总警监'])