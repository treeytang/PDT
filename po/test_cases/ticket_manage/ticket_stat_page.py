import re
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep




class Ticket_Stat(Page):
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
    # 话单统计定位
    ticker_stat_loc = (By.XPATH, '//*[@id="menu600"]/div[2]/ul/li[3]/a')
    # 系统提示弹窗定位
    hint_cancel = (By.CLASS_NAME, 'jbox-close')
    # 嵌套页面定位
    follow_iframe = 'mainFrame'

    #iframe页面话单统计定位
    stat_loc = (By.LINK_TEXT, '话单统计')
    #iframe页面队号统计定位
    teamNum_stat_loc = (By.LINK_TEXT, '队号统计')
    #iframe页面基站占忙比
    rcu_occupied_loc = (By.LINK_TEXT, '基站占忙比')


    #以下为对号统计页面元素
    #表 队号定位
    teamNum_loc = (By.ID, 'teamNumber')
    #表 用户号码定位
    userNum_loc = (By.XPATH, '//*[@id="contentTabledetail"]/tbody/tr/td[1]')




    #当点击话单统计后默认进入嵌套页面中的话单查询页面
    def come_page(self):
        #进入表单iframe公用函数
        self.find_element(*self.ticket_come_loc).click()
        sleep(1)
        self.find_element(*self.hint_cancel).click()
        self.find_element(*self.ticker_stat_loc).click()
        sleep(1)
        self.switch_frame(self.follow_iframe)




    def come_page_verify(self):
        #进入表单验证
        self.come_page()
        l = []
        msg = self.find_element(*self.stat_loc).text
        msg1 = self.find_element(*self.teamNum_stat_loc).text
        msg2 = self.find_element(*self.rcu_occupied_loc).text
        l.append(msg)
        l.append(msg1)
        l.append(msg2)
        return l


    def teamNum_stat(self):
        #进入队号统计页面 验证队号唯一性
        self.come_page()
        self.find_element(*self.teamNum_stat_loc).click()
        s = self.find_elements(*self.teamNum_loc)
        lst = []
        for num in s:
            lst.append(num.text)
        num1 = len(lst)
        num2 = len(set(lst))
        if num1 != num2:
            return False
        else:
            return True


    def userNum_stat(self):
        #进入队号统计页面 验证用户号码唯一性
        self.come_page()
        self.find_element(*self.teamNum_stat_loc).click()
        s = self.find_elements(*self.teamNum_loc)
        for team_num in s:
            team_num.click()
            l = []
            users = self.find_elements(*self.userNum_loc)
            for user in users:
                l.append(user)
            if len(l) != len(set(l)):
                return False
        return True


    #基站占忙比页面基站选择下拉定位
    rcu_choice = (By.XPATH, '//*[@id="s2id_stationSelect"]/a/span[2]')
    #基站占忙比页面基站选择 输入框定位
    rcu_input = (By.XPATH, '//*[@id="select2-drop"]/div/input')
    #基站占忙比页面时间输入框定位
    time_input = (By.ID, 'time')
    #查询按钮定位
    query_button = (By.ID, 'queryButton')


    def come_rcu_occupied_1(self):
        #进入基站占忙比页面 输入正确基站时间查询
        self.come_page()
        self.find_element(*self.rcu_occupied_loc).click()
        self.find_element(*self.rcu_choice).click()
        self.find_element(*self.rcu_input).send_keys('武侯测试')
        self.send_enter(*self.rcu_input)
        self.find_element(*self.time_input).send_keys('2018-12-12 16')
        self.find_element(*self.query_button).click()
        sleep(3)
        element = WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mask"]/div')))

        if element:
            return True
        return False

    def come_rcu_occupied_2(self):
        #进入基站占忙比页面 输入正确基站时间查询
        self.come_page()
        self.find_element(*self.rcu_occupied_loc).click()
        self.find_element(*self.rcu_choice).click()
        self.find_element(*self.rcu_input).send_keys('武侯测试')
        self.send_enter(*self.rcu_input)
        self.find_element(*self.time_input).send_keys('2019-12-12 16')
        self.find_element(*self.query_button).click()
        msg = self.find_element(*(By.XPATH, '//*[@id="mask"]/div')).text
        return msg


