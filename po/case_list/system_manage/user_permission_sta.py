from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.system_page.user_permission_page import User_permission
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        User_permission(self.driver).user_login(username, password)

    def test_1_come_user_manage(self):
        '''检查进入用户权限页面 验证'''
        self.user_login(username="thy", password="admin")
        msg = User_permission(self.driver).come_iframe_verify()
        self.assertEqual(msg.strip(), '权限列表')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_verify_user_num(self):
        '''检查进入用户权限页面 显示数量 验证'''
        self.user_login(username="thy", password="admin")
        msg = User_permission(self.driver).verify_user_num()
        self.assertEqual(msg.strip(), '5')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_add_permission(self):
        '''检查进入用户权限页面并进行 权限添加 验证'''
        self.user_login(username="thy", password="admin")
        msg = User_permission(self.driver).add_permission()
        self.assertEqual(msg.strip(), '自动化测试')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_modify_permission(self):
        '''检查进入用户权限页面 权限修改 验证'''
        self.user_login(username="thy", password="admin")
        msg = User_permission(self.driver).modify_permission()
        self.assertEqual(msg, True)