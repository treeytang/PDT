from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.ticket_manage.user_followup_page import User_FollowUp
import HTMLTestRunner




class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        User_FollowUp(self.driver).user_login(username, password)

    def test_come_follow_page_verify(self):
        '''是否进入用户追踪页面'''
        self.user_login(username="admin", password="admin")
        msg = User_FollowUp(self.driver).come_page_verify()
        self.assertEqual(msg.strip(), "请输入需要查询的用户")
        picture.insert_img(self.driver, "user_pwd_true.png")


    def test_query_user(self):
        #输入正确的用户名时间进行搜索
        self.user_login(username="admin", password="admin")
        msg = User_FollowUp(self.driver).query_user_verify_0()
        self.assertEqual(msg.strip(), "445101")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_query_user_1(self):
        # 输入正确的用户名 不合法的时间（2019-11）进行搜索
        self.user_login(username="admin", password="admin")
        msg = User_FollowUp(self.driver).query_user_verify_1()
        self.assertEqual(msg.strip(), "没有找到匹配项")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_query_user_2(self):
        #输入正确的用户名时间进行搜索 比对语音数据
        self.user_login(username="admin", password="admin")
        msg = User_FollowUp(self.driver).query_user_verify_2()
        self.assertEqual(msg.strip(), "20876")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_query_user_3(self):
        # 输入正确的用户名时间进行搜索 比对语音数据
        self.user_login(username="admin", password="admin")
        msg = User_FollowUp(self.driver).query_user_verify_3()
        self.assertEqual(msg.strip(), "654")
        picture.insert_img(self.driver, "user_pwd_true.png")


    def test_query_user_4(self):
        # 输入正确的用户名时间进行搜索 比对语音数据
        self.user_login(username="admin", password="admin")
        msg = User_FollowUp(self.driver).query_user_verify_4()
        self.assertEqual(msg.strip(), "1195")
        picture.insert_img(self.driver, "user_pwd_true.png")