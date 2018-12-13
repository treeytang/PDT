from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.ticket_manage import Ticket_Manage_Query
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Ticket_Manage_Query(self.driver).user_login(username, password)

    def test_come_ticket_query_verify(self):
        '''是否进入话单查询页面'''
        self.user_login(username="admin", password="admin")
        msg = Ticket_Manage_Query(self.driver).come_query_verify()
        self.assertEqual(msg.strip(), "话单查询")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_ticket_query(self):
        '''话单查询页面列表显示数量与实际数量比较'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_num_verify()
        self.assertEqual(msg,'ok')
        picture.insert_img(self.driver, 'user_query.png')

    def test_input_num_query(self):
        '''指定每页显示数量与实际显示数量比较'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).page_define_num()
        self.assertEqual(msg,'ok')
        picture.insert_img(self.driver, 'user_num_query.png')



