import re
import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep




class Ticket_Manage_Query(Page):
    '''
        话单管理--话单查询页面
        默认进入到话单查询页面
    '''


    #进入话单管理页面--默认进入话单查询  定位
    ticket_come_loc = (By.XPATH, '//*[@id="menu600"]/div[1]/a')
    #切换到嵌套表单定位
    ticket_iframe_id = 'mainFrame'
    #验证进入表单定位
    iframe_verify = (By.CLASS_NAME, 'panel-heading')
    #系统提示弹窗定位
    hint_cancel = (By.CLASS_NAME, 'jbox-close')


    # 查询  起始时间查询定位
    start_time_loc = (By.ID, 'startTime-th')
    # 查询 1 天定位
    one_day_loc = (By.XPATH, '//*[@id="oneday"]/a')
    # 查询 7 天定位
    one_week_loc = (By.XPATH, '//*[@id="oneweek"]/a')
    # 查询 30 天定位
    one_month_loc = (By.XPATH, '//*[@id="onemonth"]/a')
    # 查询 自定义 天定位
    custom_loc = (By.XPATH, '//*[@id="custom"]/a')

    #定义一页显示多少条定位
    page_any_loc = (By.ID,"page_any")
    #以一条为基准，获取条数定位
    page_num_loc = (By.XPATH, '//*[@id="pagination"]/ul/li[11]/a')



    # 话单查询 列表显示数量与实际数量 行定位
    table_line = (By.CLASS_NAME, 'contentbody')
    # 翻页定位
    next_page = (By.LINK_TEXT, '下一页 »')
    #查询到的数量定位
    query_num_loc = (By.XPATH, '//*[@id="pagination"]/ul')#//*[@id="pagination"]/ul







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




    #查询数量
    def query_num(self):
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.script(js)
        sleep(10)
        js = "var q=document.documentElement.scrollTop=1000000"
        self.script(js)
        return self.find_element(*self.query_num_loc)






    # 验证进入话单管理_话单查询页面
    def come_query_verify(self):
        self.find_element(*self.ticket_come_loc).click()
        # 进入到右侧表单
        self.switch_frame(self.ticket_iframe_id)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.script(js)
        # # 出现弹窗，返回上一层表单
        # self.switch_to_default()
        # if self.find_element(*self.hint_cancel):
        #     # 关闭提示窗口
        #     self.find_element(*self.hint_cancel).click()
        #     self.switch_frame(self.ticket_iframe_id)
        #     js = "var q=document.documentElement.scrollTop=10000"
        #     self.script(js)
        # sleep(2)
        # self.find_element(*self.next_page).click()
        return self.find_element(*self.iframe_verify).text



    #验证话单查询显示数量与实际数量   30  天
    def query_num_verify(self):
        self.find_element(*self.ticket_come_loc).click()
        # 进入到右侧表单
        self.switch_frame(self.ticket_iframe_id)

        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        # 出现弹窗，返回上一层表单
        self.switch_to_default()
        if self.find_element(*self.hint_cancel):
            # 关闭提示窗口
            self.find_element(*self.hint_cancel).click()
            self.switch_frame(self.ticket_iframe_id)
            js = "var q=document.documentElement.scrollTop=10000"
            self.script(js)
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.one_week_loc).click()
        a = self.query_num().text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d',a))
        print("查询条数共计：%s条"%s)
        self.find_element(*self.page_any_loc).send_keys("1")
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        query_num = self.find_element(*self.page_num_loc).text
        if str(s)==query_num:
            return 'ok'
        else:
            return 'xxx'
        # self.driver.send_keys(Keys.ESCAPE)
        # cleck_num = 0
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.script(js)
        # while self.find_element(*self.next_page):
        #     s = self.find_elements(*self.table_line)
        #     for i in s:
        #         cleck_num += 1
        #     js = "var q=document.documentElement.scrollTop=10000"
        #     self.script(js)
        #     if self.find_element(*self.next_page).is_enabled():
        #         self.find_element(*self.next_page).click()
        #     else:
        #         break
        #     # if self.find_element(*self.next_page):
        #     #     if not self.find_element(*self.next_page).is_enabled():
        #     #         break
        #     #     self.find_element(*self.next_page).click()
        #     #
        #     # else:
        #     #     break
        # sleep(2)
        # self.find_element(*self.next_page).click()


    def page_define_num(self):
        self.find_element(*self.ticket_come_loc).click()
        # 进入到右侧表单
        self.switch_frame(self.ticket_iframe_id)

        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        # 出现弹窗，返回上一层表单
        self.switch_to_default()
        if self.find_element(*self.hint_cancel):
            # 关闭提示窗口
            self.find_element(*self.hint_cancel).click()
            self.switch_frame(self.ticket_iframe_id)
            js = "var q=document.documentElement.scrollTop=10000"
            self.script(js)
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.one_week_loc).click()
        input_num = str(random.randrange(1,10))
        print(input_num)
        self.find_element(*self.page_any_loc).send_keys(input_num)
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        num = self.find_elements(*self.table_line)
        check_num = 0
        for i in num:
            check_num += 1
        print(check_num)
        if input_num==check_num:
            return "ok"
        else:
            return "xxx"
