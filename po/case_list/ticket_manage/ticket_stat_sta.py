from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.ticket_manage.ticket_stat_page import Ticket_Stat
import HTMLTestRunner




class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Ticket_Stat(self.driver).user_login(username, password)

    def test_come_page_verify(self):
        '''是否进入话单统计页面'''
        self.user_login(username="admin", password="admin")
        msg = Ticket_Stat(self.driver).come_page_verify()
        self.assertEqual(msg, ['话单统计', '队号统计', '基站占忙比'])
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_teamNum_verify(self):
        '''进入队号统计页面 验证对号唯一性'''
        self.user_login(username="admin", password="admin")
        msg = Ticket_Stat(self.driver).teamNum_stat()
        self.assertEqual(msg, True)
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_userNum_verify(self):
        '''进入队号统计页面 验证用户号唯一性'''
        self.user_login(username="admin", password="admin")
        msg = Ticket_Stat(self.driver).userNum_stat()
        self.assertEqual(msg, True)
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_rcu_occupied_query_verify(self):
        '''进入基站占忙比页面 输入正确的基站时间进行查询'''
        self.user_login(username='admin', password='admin')
        msg = Ticket_Stat(self.driver).come_rcu_occupied_1()
        self.assertEqual(msg, True)

    def test_rcu_occupied_query_verify_1(self):
        '''进入基站占忙比页面 输入正确的基站时间进行查询'''
        self.user_login(username='admin', password='admin')
        msg = Ticket_Stat(self.driver).come_rcu_occupied_2()
        self.assertEqual(msg.strip(), '无数据')