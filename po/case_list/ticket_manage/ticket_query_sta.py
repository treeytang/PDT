from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.ticket_manage.ticket_manage_page import Ticket_Manage_Query
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Ticket_Manage_Query(self.driver).user_login(username, password)


    def test_come_ticket_query_verify(self):
        '''是否进入话单查询页面'''
        self.user_login(username="t", password="admin")
        msg = Ticket_Manage_Query(self.driver).come_query_verify()
        self.assertEqual(msg.strip(), "话单查询")


    # def test_ticket_query(self):
    #     '''话单查询页面列表显示数量与实际数量比较'''
    #     self.user_login(username='thy', password='admin')
    #     msg = Ticket_Manage_Query(self.driver).query_num_verify()
    #     self.assertEqual(msg,'ok')
    #     picture.insert_img(self.driver, 'user_query.png')


    def test_input_num_query(self):
        '''指定每页显示数量与实际显示数量比较'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).page_define_num()
        self.assertEqual(msg,'ok')



    def test_custom_query1(self):
        '''自定义时间查询 正确的起止时间'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).custom_time_query1()
        self.assertEqual(msg,"pass")
        picture.insert_img(self.driver, 'custom_query.png')

    def test_custom_query2(self):
        '''自定义时间查询 正确的起始时间，超期的结束时间(在自动化操作中使用的是js控制，在实际中是无法选择超期时间的)'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).custom_time_query2()
        self.assertEqual(msg,"pass")

    def test_custom_query3(self):
        '''自定义时间查询 正确的起始时间，超期的结束时间'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).custom_time_query3()
        self.assertEqual(msg,"pass")

    def test_custom_query4(self):
        '''自定义时间查询 超期的起始时间，正确的结束时间'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).custom_time_query4()
        self.assertEqual(msg,"pass")


    def test_query_calling_voc_num(self):
        '''查询用户2019/03/01到201/04/01主叫 语音 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_calling_voc_num()
        self.assertEqual(msg, "58")

    def test_query_calling_reg_num(self):
        '''查询用户2019/03/01到201/04/01主叫 注册/注销 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_calling_reg_num()
        self.assertEqual(msg, "70")

    def test_query_calling_sms_num(self):
        '''查询用户2019/03/01到201/04/01主叫 短信 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_calling_sms_num()
        self.assertEqual(msg, "8")


    def test_query_calling_gps_num(self):
        '''查询用户2019/03/01到2019/04/01主叫 gps 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_calling_gps_num()
        self.assertEqual(msg, "44")

    def test_query_calling_stun_num(self):
        '''查询用户2019/03/01到2019/04/01主叫 复活 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_calling_stun_num()
        self.assertEqual(msg, "85")


    def test_query_calling_grp_num(self):
        '''查询用户2019/03/01到2019/04/01主叫 重组/去重组 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_calling_grp_num()
        self.assertEqual(msg, "6")


    def test_query_called_voc_num(self):
        '''查询用户2019/03/01到2019/04/01被叫 语音 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_called_voc_num()
        self.assertEqual(msg, "99")


    def test_query_called_reg_num(self):
        '''查询用户2019/03/01到2019/04/01被叫 注册/注销 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_called_reg_num()
        self.assertEqual(msg, "70")

    def test_query_called_sms_num(self):
        '''查询用户2019/03/01到2019/04/01被叫 短信 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_called_sms_num()
        self.assertEqual(msg, "278")


    def test_query_called_gps_num(self):
        '''查询用户2019/03/01到2019/04/01被叫 gps 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_called_gps_num()
        self.assertEqual(msg, "6")


    def test_query_called_stun_num(self):
        '''查询用户2019/03/01到2019/04/01被叫 复活 数量'''
        self.user_login(username='thy', password='admin')
        msg = Ticket_Manage_Query(self.driver).query_called_stun_num()
        self.assertEqual(msg, "23")
        picture.insert_img(self.driver, 'custom_query.png')

    # def test_query_called_
