from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.user_manage.MS_manage_page import Mobile_Station
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Mobile_Station(self.driver).user_login(username, password)

    def test_come_page(self):
        '''检查进入移动台管理页面 验证'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).come_iframe_verify()
        self.assertEqual(msg.strip(), '移动用户列表')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_show_num_verify(self):
        '''检查进入移动台管理页面对显示数量的验证'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).query_num_verify()
        self.assertEqual(msg.strip(), '1000')
        picture.insert_img(self.driver, "user_pwd_true.png")


    def test_come_add_icon_verify(self):
        '''进入移动台管理页面 点击开户 进入开户界面验证'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).come_add_icon()
        self.assertEqual(msg.strip(), '移动用户--开户')
        picture.insert_img(self.driver, "user_pwd_true.png")

    def test_add_icon_verify(self):
        '''进入移动台管理页面 点击开户 进入开户界面验证'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1()
        self.assertEqual(msg.strip(), '添加成功')


    def test_add_icon_verify_1(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的正确用户'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1()
        self.assertEqual(msg.strip(), '添加成功')


    def test_add_icon_verify_1_1(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 区号最小值减一：327'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_1()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_2(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 区号最大值加一：807'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_2()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_3(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 输入英文：aa'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_3()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_4(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 输入中文：警察'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_4()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_5(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的队号 最大值加一：90'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_5()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_6(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的队号 最小值减一：19'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_6()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_7(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 4位区号'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_7()
        self.assertEqual(msg, True)


    def test_add_icon_verify_1_8(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的区号 2位区号'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_8()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_9(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的队号 输入英文:aa'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_9()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_10(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的队号 输入中文:警察'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_10()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_11(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的个号 最大值加一：900'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_11()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_12(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的个号 最小值减一：199'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_12()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_13(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的个号 输入英文:aaa'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_13()
        self.assertEqual(msg, True)

    def test_add_icon_verify_1_14(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的用户  错误的个号  输入中文:一二三'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_1_14()
        self.assertEqual(msg, True)


    def test_add_icon_verify_2(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个已注册的正确用户'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_2()
        self.assertEqual(msg, True)


    def test_add_icon_verify_3(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个未注册的正确用户 实名制信息相关选择(边界值 全选第一个)'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_3()
        self.assertEqual(msg, ['海格恒通', '女', '交警', '二级警员'])


    def test_add_icon_verify_4(self):
        '''进入移动台管理页面 点击开户 进入开户界面添加一个已注册的正确用户 实名制信息相关选择(边界值 全选最后一个个)'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).add_icon_4()
        self.assertEqual(msg, ['科立讯', '男', '巡警', '总警监'])


    def test_come_matrix_verify(self):
        '''进入移动台管理页面 点击切换至矩阵显示模式 进入矩阵显示页面'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).show_matrix()
        self.assertEqual(msg, True)


    #用户映射功能模块

    def test_user_map_show_num(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面 验证显示数量'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num()
        self.assertEqual(msg.strip(), '4')

    def test_user_map_show_num_1(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面 验证分页显示显示数量'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_1()
        self.assertEqual(msg.strip(), '1')

    def test_user_map_show_num_2(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 800 41 200/210  800 41 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_1(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的区号 区号最小值减一：327 327 41 200/210  327 41 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_1()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_2(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的区号 区号最大值加一：807  807 41 200/210  807 41 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_2()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_3(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的区号 区号为英文字母：aaa  aaa 41 200/210  aaa 41 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_3()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_4(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的区号 区号为中文：警察  警察 41 200/210  警察 41 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_4()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_5(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的区号 区号为两位数字：33  33 41 200/210  33 41 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_5()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_6(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的队号 队号为最小值减一：19  328 19 200/210  328 19 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_6()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_7(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的队号 队号为最大值加一：19  328 90 200/210  328 90 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_7()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_8(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的队号 队号为英文字母：aa  328 aa 200/210  328 aa 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_8()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_9(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的队号 队号为中文：警察  328 警察 200/210  328 警察 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_9()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_10(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的队号 队号为符号：%^  328 %^ 200/210  328 %^ 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_10()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_11(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的个号 个号为最大值加一：900  328 40 900/355  328 40 355/900'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_11()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_12(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的个号 个号为最小值减一：199  328 40 199/355  328 40 355/199'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_12()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_13(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的个号 个号为英文字母：aaa  328 40 aaa/355  328 40 355/aaa'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_13()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_14(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的个号 个号为中文：成都市  328 40 成都市/355  328 40 355/成都市'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_14()
        self.assertEqual(msg, True)

    def test_user_map_show_num_2_15(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面  配置一条新的用户号码映射范围 错误的个号 个号为符号：%^&  328 40 %^&/355  328 40 355/%^&'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_2_15()
        self.assertEqual(msg, True)

    def test_user_map_show_num_3(self):
        '''进入移动台管理页面 点击用户映射 进入用户映射页面 配置一条已存在的用户号码映射范围 445 30 200/210 445 30 300/310'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).user_map_show_num_3()
        self.assertEqual(msg, True)

    def test_local_online_user(self):
        '''进入移动台管理页面 点击本地在线用户 进入本地在线用户验证'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).local_online_user()
        self.assertEqual(msg.strip(), '3')

    def test_local_online_user_1(self):
        '''进入移动台管理页面 点击本地在线用户 进入本地在线用户验证分页'''
        self.user_login(username="admin", password="admin")
        msg = Mobile_Station(self.driver).local_online_user_page()
        self.assertEqual(msg.strip(), '1')
