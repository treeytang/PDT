import re
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class Real_Alarm_Query(Page):
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

    # 以下为登录公用函数
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

    #该页面默认进入实时告警页面 需定位告警查询元素
    #告警管理定位
    alarm_manage_loc = (By.XPATH, '//*[@id="menu500"]/div[1]/a')
    #告警查询定位
    alarm_query_loc = (By.LINK_TEXT, '实时告警')
    #嵌套页面定位
    iframe_id_loc = 'mainFrame'

    #进入页面验证点定位
    verify_loc = (By.CLASS_NAME, 'panel-heading')
    #数量定位
    real_alarm_num = (By.CLASS_NAME, 'showName')



    #获取告警数量
    def get_alarm_num(self):
        self.switch_frame(self.iframe_id_loc)
        num1 = int(self.find_element(*(By.XPATH, '//*[@id="serious-alarm"]/a')).text)
        num2 = int(self.find_element(*(By.XPATH, '//*[@id="common-alarm"]/a')).text)
        num3 = int(self.find_element(*(By.XPATH, '//*[@id="slight-alarm"]/a')).text)
        num = num1 + num2 + num3
        self.switch_to_default()
        return num



    def come_iframe_page(self):
        #公用函数 进入iframe页面
        self.find_element(*self.alarm_manage_loc).click()
        self.find_element(*self.alarm_query_loc).click()
        self.switch_frame(self.iframe_id_loc)
        sleep(3)

    def come_page_verify(self):
        #进入iframe页面验证
        self.come_iframe_page()
        msg = self.find_element(*self.verify_loc).text
        return msg

    def real_alarm_verify(self):
        #实时告警数量验证
        num = self.get_alarm_num()
        self.come_iframe_page()
        msg = self.find_elements(*self.real_alarm_num)
        s = (str(len(msg)))
        l = [s, str(num)]
        return l
