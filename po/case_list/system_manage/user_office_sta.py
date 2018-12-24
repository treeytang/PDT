from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.system_page.office_page import User_Office
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        User_Office(self.driver).user_login(username, password)

    def test_1_come_user_office(self):
        '''检查进入用户单位页面'''
        self.user_login(username="thy", password="admin")
        msg = User_Office(self.driver).come_user_office_verify()
        self.assertEqual(msg.strip(), "省公安厅")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_2_office_add(self):
        '''进入单位添加页面 循环添加十各单位 与实际显示成功添加的单位检验'''
        self.user_login(username="thy", password="admin")
        msg = User_Office(self.driver).office_add_verify()
        self.assertEqual(msg.strip(), "10")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_3_office_del(self):
        '''单位添加页面 循环删除通过单位添加后的省厅下级单位 实际显示与实际删除对比检验'''
        self.user_login(username="thy", password="admin")
        msg = User_Office(self.driver).office_del_verify()
        self.assertEqual(msg, True)
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_4_office_add(self):
        '''进入添加下级单位 循环添加十各单位 与实际显示成功添加的单位检验'''
        self.user_login(username="thy", password="admin")
        msg = User_Office(self.driver).head_add_next_office_verify()
        self.assertEqual(msg.strip(), "10")
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_5_office_del(self):
        '''单位添加页面 循环删除通过添加下级单位后的省厅下级单位 实际显示与实际删除对比检验'''
        self.user_login(username="thy", password="admin")
        msg = User_Office(self.driver).office_del_verify()
        self.assertEqual(msg, True)
        picture.insert_img(self.driver, "user_pwd_true.png")


    def test_6_add_show(self):
        '''检测添加单位后该是否显示该单位'''
        self.user_login(username="thy", password="admin")
        msg = User_Office(self.driver).add_show_verify()
        self.assertEqual(msg.strip(), "测试成都")
        picture.insert_img(self.driver, "user_pwd_true.png")