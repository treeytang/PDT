from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.alarm_manage.real_time_page import Real_Alarm_Query
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Real_Alarm_Query(self.driver).user_login(username, password)


    def test_come_real_alarm_verify(self):
        '''是否进入实时告警页面验证'''
        self.user_login(username="admin", password="admin")
        msg = Real_Alarm_Query(self.driver).come_page_verify()
        self.assertEqual(msg.strip(), "实时告警")
        picture.insert_img(self.driver, "user_pwd_true.png")


    def test_real_alarm_num_verify(self):
        '''进入告警查询页面 验证显示数量'''
        self.user_login(username="admin", password="admin")
        msg = Real_Alarm_Query(self.driver).real_alarm_verify()
        real,expect = msg[0],msg[1]
        self.assertEqual(real.strip(), expect.strip())
        picture.insert_img(self.driver, "user_pwd_true.png")