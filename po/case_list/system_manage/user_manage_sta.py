from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.system_page.user_manage_page import User_manage
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        User_manage(self.driver).user_login(username, password)

    def test_1_come_user_manage(self):
        '''检查进入用户管理页面验证'''
        self.user_login(username="thy", password="admin")
        msg = User_manage(self.driver).come_page_verify()
        self.assertEqual(msg, True)
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_verify_user_num_verify(self):
        '''检查用户管理页面 用户显示数量验证'''
        self.user_login(username="thy", password="admin")
        msg = User_manage(self.driver).query_user_num()
        self.assertEqual(msg.strip(), '7')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_verify_input_query_user_1(self):
        '''检查用户管理页面 通过登录名模糊查询用户显示数量验证'''
        self.user_login(username="thy", password="admin")
        msg = User_manage(self.driver).input_query_1()
        self.assertEqual(msg.strip(), '2')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_verify_input_query_user_2(self):
        '''检查用户管理页面 通过姓名模糊查询用户显示数量验证'''
        self.user_login(username="thy", password="admin")
        msg = User_manage(self.driver).input_query_2()
        self.assertEqual(msg.strip(), '1')
        picture.insert_img(self.driver, "user_pwd_true.png")






