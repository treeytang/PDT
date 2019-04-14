from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.user_manage.third_party_page import ThirdParty
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        ThirdParty(self.driver).user_login(username, password)

    def test_third_user(self):
        '''检查进入第三方用户界面 验证页面显示数量'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).page_show_num()
        self.assertEqual(msg.strip(), '17')

    def test_third_user_1(self):
        '''检查进入第三方用户界面 验证分页面显示'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).paging_verify()
        self.assertEqual(msg.strip(), '1')

    def test_add_user(self):
        '''检查进入第三方用户界面 点击用户添加并保存（正确的号码、别名...）  验证是否添加成功'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).add_user()
        self.assertEqual(msg, True)

    def test_add_user_1(self):
        '''检查进入第三方用户界面 点击用户添加并保存 号码为英文'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).add_user_1()
        self.assertEqual(msg, True)

    def test_add_user_2(self):
        '''检查进入第三方用户界面 点击用户添加并保存 号码为数字+英文'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).add_user_2()
        self.assertEqual(msg, True)

    def test_add_user_3(self):
        '''检查进入第三方用户界面 点击用户添加并保存 号码为中文 '''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).add_user_3()
        self.assertEqual(msg, True)

    def test_add_user_4(self):
        '''检查进入第三方用户界面 点击用户添加并保存 号码为符号 '''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).add_user_4()
        self.assertEqual(msg, True)

    def test_add_user_5(self):
        '''检查进入第三方用户界面 点击用户添加,添加一个已存在的用户并保存 是否出现弹窗'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).add_user_5()
        self.assertEqual(msg, True)#在测试中，如果添加后直接到了列表页面，并找到了用户，那么说明没有提示窗口

    def test_del_user(self):
        '''检查进入第三方用户界面 点击删除一个用户号码 验证：是否成功删除用户'''
        self.user_login(username="admin", password="admin")
        msg = ThirdParty(self.driver).del_user()
        self.assertEqual(msg, True)