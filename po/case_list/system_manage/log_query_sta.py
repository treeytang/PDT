from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.system_page.log_query_page import Log_Query
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Log_Query(self.driver).user_login(username, password)

    def test_come_user_manage(self):
        '''检查进入用户日志查询页面验证'''
        self.user_login(username="thy", password="admin")
        msg = Log_Query(self.driver).come_iframe_verify()
        self.assertEqual(msg.strip(),'日志查询')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_log_num_verify(self):
        '''检查进入日志查询页面 验证2018/01/01--2019/01/01日志数量'''
        self.user_login(username="thy", password="admin")
        msg = Log_Query(self.driver).verify_log_num()
        self.assertEqual(msg.strip(),'9497')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_log_num_verify_1(self):
        '''检查进入日志查询页面 验证2018/01/01--2019/01/01 操作目标为System Login 日志数量'''
        self.user_login(username="thy", password="admin")
        msg = Log_Query(self.driver).verify_log_num_1()
        self.assertEqual(msg.strip(),'1077')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_log_num_verify_2(self):
        '''检查进入日志查询页面 验证2018/01/01--2019/01/01 URL为/nmp/sys/user/list 日志数量'''
        self.user_login(username="thy", password="admin")
        msg = Log_Query(self.driver).verify_log_num_2()
        self.assertEqual(msg.strip(),'1100')
        picture.insert_img(self.driver, "user_pwd_true.png")

