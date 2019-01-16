from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.user_manage.DRM_user_page import DRM_User
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        DRM_User(self.driver).user_login(username, password)

    def test_show_page_num(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 验证页面显示数量'''
        self.user_login(username="thy", password="admin")
        msg = DRM_User(self.driver).user_verity()
        self.assertEqual(msg.strip(), '16')

