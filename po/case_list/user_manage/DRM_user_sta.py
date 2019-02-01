from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.user_manage.DRM_user_page import DRM_User
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        DRM_User(self.driver).user_login(username, password)

    def test_DMR_user(self):
        '''检查进入DMR用户界面(默认进入DMR用户) 验证页面显示数量'''
        self.user_login(username="admin", password="admin")
        msg = DRM_User(self.driver).user_verify()
        self.assertEqual(msg.strip(), '16')

    def test_DMR_user_1(self):
        '''检查进入DMR用户界面(默认进入DMR用户) 验证页面分页显示数量'''
        self.user_login(username="admin", password="admin")
        msg = DRM_User(self.driver).user_verify_1()
        self.assertEqual(msg.strip(), '1')


    def test_DMR_group(self):
        '''检查进入DMR用户界面(默认进入DMR用户) 验证页面显示数量'''
        self.user_login(username="admin", password="admin")
        msg = DRM_User(self.driver).group_verify()
        self.assertEqual(msg.strip(), '28')

    def test_DMR_group_1(self):
        '''检查进入DMR用户界面(默认进入DMR用户) 验证页面显示数量'''
        self.user_login(username="admin", password="admin")
        msg = DRM_User(self.driver).group_verify_1()
        self.assertEqual(msg.strip(), '1')