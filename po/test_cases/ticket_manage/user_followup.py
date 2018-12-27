import re
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep




class User_FollowUp(Page):
    url = '/login'
    # 登录用户名的定位
    login_username_loc = (By.ID, 'username')
    # 登录密码的定位
    login_password_loc = (By.ID, 'password')
    # 登录按钮的定位
    login_button_loc = (By.ID, 'login-btn')
    # 登录错误提示的定位
    login_error_loc = (By.ID, 'loginError')
    # 登录成功用户名信息
    login_user_success_loc = (By.XPATH, '//*[@id="zhongduanshu"]/div[1]')

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一登录入口
    def user_login(self, username="testuser01", password="testgood001"):
        # 获取用户名和页面登录
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    # 进入话单管理页面--默认进入话单查询  定位
    ticket_come_loc = (By.XPATH, '//*[@id="menu600"]/div[1]/a')
    #用户追踪定位
    user_follow = (By.XPATH, '//*[@id="menu600"]/div[2]/ul/li[2]/a')
    # 系统提示弹窗定位
    hint_cancel = (By.CLASS_NAME, 'jbox-close')
    #嵌套页面定位
    follow_iframe = 'mainFrame'
    #页面检验定位
    verify_loc = (By.XPATH, '//*[@id="container"]/div[3]/div')

    #用户名或号码输入框定位
    input_box_loc = (By.ID, 'callNo')
    #年月选择定位
    year_moth_loc = (By.XPATH, '//*[@id="s2id_monthSelect"]/a/span[2]')
    #年月输入框定位
    year_moth_input_loc = (By.XPATH, '//*[@id="select2-drop"]/div/input')
    #没有找到匹配项提示定位
    no_match = (By.XPATH, '//*[@id="select2-drop"]/ul/li')

    #用户名验证定位
    user_verify_loc = (By.XPATH, '//*[@id="track-detail"]/tbody/tr[1]/td[2]')
    #组呼数量定位
    group_call_num = (By.XPATH, '//*[@id="track-data-summary"]/tr[1]/td[2]')
    #单呼数量定位
    only_call_num = (By.XPATH, '//*[@id="track-data-summary"]/tr[2]/td[2]')
    #注册数量
    regist_num_loc = (By.XPATH, '//*[@id="track-data-summary"]/tr[3]/td[2]')
    #短信数量
    sms_num_loc = (By.XPATH, '//*[@id="track-data-summary"]/tr[5]/td[2]')


    def come_page(self):
        #进入表单公用函数
        self.find_element(*self.ticket_come_loc).click()
        sleep(1)
        self.find_element(*self.hint_cancel).click()
        self.find_element(*self.user_follow).click()
        sleep(1)
        self.switch_frame(self.follow_iframe)



    def come_page_verify(self):
        #进入表单验证
        self.come_page()
        verify = self.find_element(*self.verify_loc).text
        return verify




    def query_user_verify(self):
        self.come_page()
        self.find_element(*self.input_box_loc).send_keys('445101')
        sleep(1)
        self.find_element(*self.year_moth_loc).click()
        self.find_element(*self.year_moth_input_loc).send_keys('2018-11')
        self.send_enter(*self.year_moth_input_loc)
        sleep(3)

    def query_user_verify_0(self):
        #输入用户名，时间公用函数
        self.query_user_verify()
        msg = self.find_element(*self.user_verify_loc).text
        return msg

    def query_user_verify_1(self):
        #输入正确的用户名 错误的时间 验证
        self.come_page()
        self.find_element(*self.input_box_loc).send_keys('445101')
        sleep(1)
        self.find_element(*self.year_moth_loc).click()
        self.find_element(*self.year_moth_input_loc).send_keys('2019-11')
        msg = self.find_element(*self.no_match).text
        return msg


    def query_user_verify_2(self):
        # 输入正确的用户名时间 比对语音数据
        self.query_user_verify()
        group = self.find_element(*self.group_call_num).text
        only = self.find_element(*self.only_call_num).text
        num = int(group)+int(only)
        return str(num)


    def query_user_verify_3(self):
        # 输入正确的用户名时间 比对注册数据
        self.query_user_verify()
        regist_num = self.find_element(*self.regist_num_loc).text
        return regist_num

    def query_user_verify_4(self):
        #输入正确的用户名时间 对比短信数据
        self.query_user_verify()
        sms_num = self.find_element(*self.sms_num_loc).text
        return sms_num
