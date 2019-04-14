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
        self.user_login(username="t", password="admin")
        msg = User_manage(self.driver).come_page_verify()
        self.assertEqual(msg, True)

    def test_verify_user_num_verify(self):
        '''检查用户管理页面 验证用户显示数量'''
        self.user_login(username="t", password="admin")
        msg = User_manage(self.driver).query_user_num()
        self.assertEqual(msg.strip(), '4')

    def test_verify_input_query_user_1(self):
        '''检查用户管理页面 通过登录名模糊查询 查询登录名中含有w的用户数量'''
        self.user_login(username="t", password="admin")
        msg = User_manage(self.driver).input_query_1()
        self.assertEqual(msg.strip(), '1')


    def test_verify_input_query_user_2(self):
        '''检查用户管理页面 通过登录名模糊查询 查询姓名名中含有“管理员”的用户数量'''
        self.user_login(username="t", password="admin")
        msg = User_manage(self.driver).input_query_2()
        self.assertEqual(msg.strip(), '1')


    def test_add_user_verify(self):
        '''检查用户管理页面 用户添加，和删除用户 验证'''
        self.user_login(username='t', password='admin')
        msg = User_manage(self.driver).add_user()
        self.assertEqual(msg, True)