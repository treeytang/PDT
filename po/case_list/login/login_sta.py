# from time import sleep
# import unittest, random, sys,time
# from comm import myunit, picture
# from test_cases.login_page import login
# import HTMLTestRunner
#
# class LoginTest(myunit.MyTest):
#
#     '''
#     测试用户登录
#     '''
#
#     def user_login_verify(self, username="", password=""):
#         login(self.driver).user_login(username, password)
#
#     def test_login1(self):
#         '''用户名、密码为空登录'''
#         self.user_login_verify()
#         po = login(self.driver)
#         self.assertEqual(po.login_error_hint(), '验证码错误, 请重试.')
#         picture.insert_img(self.driver, "user_pawd_empty.jpg")
#
#     def test_login2(self):
#         '''用户名正确，密码为空登录验证'''
#         self.user_login_verify(username="ces")
#         po = login(self.driver)
#         self.assertEqual(po.login_error_hint(), "用户名或密码不能为空")
#         picture.insert_img(self.driver,"pawd_empty.jpg")
#
#     def test_login3(self):
#         '''用户名为空，密码正确'''
#         self.user_login_verify(password="admin")
#         po = login(self.driver)
#         self.assertEqual(po.login_error_hint(),"验证码错误, 请重试.")
#         picture.insert_img(self.driver, "user_empty.jpg")
#
#     def test_login4(self):
#         '''用户名和密码不匹配'''
#         # character = random.choice('abcdefghijklmnopqrstuvwxyz')
#         # username = "sdw" + character
#         self.user_login_verify(username='admin', password="admin1")
#         po = login(self.driver)
#         self.assertEqual(po.login_error_hint(), "验证码错误, 请重试.")
#         picture.insert_img(self.driver, "user_pass_error.jpg")
#
#     def test_login5(self):
#         '''用户名、密码正确 admin admin'''
#         self.user_login_verify(username="admin" , password="admin")
#         sleep(3)
#
#         po = login(self.driver)
#         self.assertEqual(po.login_user_success(), '本地在线用户')
#         picture.insert_img(self.driver, "user_pwd_true.jpg")