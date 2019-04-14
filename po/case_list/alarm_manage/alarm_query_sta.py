from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.alarm_manage.alarm_query_page import Alarm_Query
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Alarm_Query(self.driver).user_login(username, password)


    def test_come_ticket_query_verify(self):
        '''进入告警查询页面验证'''
        self.user_login(username="admin", password="admin")
        msg = Alarm_Query(self.driver).come_alarm_query_verify()
        self.assertEqual(msg.strip(), "告警查询")


    def test_paging_verify(self):
        '''自定义分页显示数量（每页显示1条）'''
        self.user_login(username="admin", password="admin")
        msg = Alarm_Query(self.driver).paging_verify()
        self.assertEqual(msg.strip(), "1")

    def test_custom_time_quert(self):
        '''自定义时间查询 2019-03-01 00:00:00-----2019-03-31 23:59:59'''
        self.user_login(username="admin", password="admin")
        msg = Alarm_Query(self.driver).custom_time_verify_0()
        self.assertEqual(msg.strip(), "17")


    def test_custom_time_quert_1(self):
        '''自定义时间查询 2019-03-01 00:00:00-----2019-03-31 23:59:59 告警等级为严重得数量'''
        self.user_login(username="admin", password="admin")
        msg = Alarm_Query(self.driver).custom_time_verify_1()
        self.assertEqual(msg.strip(), "11")

    #该用例暂时未启用，无相应的数据进行检验
    # def test_custom_time_quert_2(self):
    #     '''自定义时间查询 2019-03-01 00:00:00-----2019-03-31 23:59:59 告警等级为一般得数量'''
    #     self.user_login(username="admin", password="admin")
    #     msg = Alarm_Query(self.driver).custom_time_verify_2()
    #     self.assertEqual(msg.strip(), "0")


    def test_custom_time_query_3(self):
        '''自定义时间查询 2018-01-01 00:00:00-----2018-12-29 23:59:59 告警等级为轻微得数量'''
        self.user_login(username="admin", password="admin")
        msg = Alarm_Query(self.driver).custom_time_verify_3()
        self.assertEqual(msg.strip(), "6")


    def test_network_event_log(self):
        '''进入网络事件日志'''
        self.user_login(username="admin", password="admin")
        msg = Alarm_Query(self.driver).network_event_log()
        self.assertEqual(msg.strip(), "告警描述")
        picture.insert_img(self.driver, "user_pwd_true.png")
