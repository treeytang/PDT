import re
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class Alarm_Query(Page):
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
    alarm_query_loc = (By.LINK_TEXT, '告警查询')
    #嵌套页面定位
    iframe_id_loc = 'mainFrame'
    #起始时间定位
    sta_end_time_loc = (By.ID, 'startTime-th')
    #自定义时间定位
    custom_time_loc = (By.XPATH, '//*[@id="custom"]/a')
    #开始世界输入框定位
    start_time_loc = (By.ID, 'startDate')
    #结束时间输入框定位
    end_time_loc = (By.ID, 'endDate')
    # 定义一页显示多少条定位
    page_any_loc = (By.ID, "page_any")
    # 查询到的数量定位
    query_num_loc = (By.XPATH, '//*[@id="pagination"]/ul')  # //*[@id="pagination"]/ul
    #告警等级定位
    alarm_level_loc = (By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[5]')
    #告警等级严重定位
    alarm_level_serious = (By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[5]/div[3]/div[2]/span')
    #告警等级一般定位
    alarm_level_generic = (By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[5]/div[3]/div[3]/span')
    # 告警等级一般定位
    alarm_level_slight = (By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[5]/div[3]/div[4]/span')

    # 查询 自定义 天定位
    custom_loc = (By.XPATH, '//*[@id="custom"]/a')
    # 自定义查询结束输入框定位
    end_date_loc = (By.ID, "endDate")
    # 自定义时间选择框嵌套页面定位
    custom_iframe = (By.XPATH, '/html/body/div[2]/iframe')
    # 开始时间确定按钮定位
    custom_submit_loc = (By.ID, 'dpOkInput')

    def come_iframe_comm(self):
        #   公用函数   进入告警查询页面
        self.find_element(*self.alarm_manage_loc).click()
        self.find_element(*self.alarm_query_loc).click()
        self.switch_frame(self.iframe_id_loc)

    def custom_time_query(self):
        self.come_iframe_comm()
        self.find_element(*self.sta_end_time_loc).click()
        self.find_element(*self.custom_time_loc).click()



    def come_alarm_query_verify(self):
        #进入告警查询页面验证
        self.come_iframe_comm()
        msg = self.find_element(*(By.LINK_TEXT, '告警查询')).text
        return msg

    def custom_time_query_comm(self):
        #公用函数  自定义时间查询 start_time:2018-01-01 00:00:00  end_time:2018-12-29 23:59:59
        self.come_iframe_comm()
        self.find_element(*self.sta_end_time_loc).click()
        self.find_element(*self.custom_time_loc).click()
        self.find_element(*self.start_time_loc).send_keys('2019-03-01 00:00:00')
        self.find_element(*self.custom_time_loc).click()
        self.find_element(*self.end_time_loc).send_keys('2019-03-31 23:59:59')
        self.find_element(*self.custom_time_loc).click()
        self.find_element(*self.end_time_loc).click()
        self.send_enter(*self.end_time_loc)
        #每页显示多少条
        self.find_element(*self.page_any_loc).send_keys("1")
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)

    def query_num(self):
        a = self.find_element(*self.query_num_loc).text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d', a))
        print("查询条数共计：%s条" % s)
        return s

    # 指定时间查询被叫用户对应的类型
    def designate_time_called(self, called_user='', start_time="2019-03-01 00:00:00", end_time="2019-03-31 23:59:59"):
        self.come_iframe_comm()
        self.find_element(*self.sta_end_time_loc).click()
        ActionChains(self.driver).move_to_element(self.find_element(*self.custom_loc)).perform()
        self.find_element(*self.custom_loc).click()
        js = "document.querySelector('#startDate').value = '{}'".format(start_time)
        self.script(js)
        js = "document.querySelector('#endDate').value = '{}'".format(end_time)
        self.script(js)
        self.find_element(*self.end_date_loc).click()
        self.switch_to_default()
        self.switch_frame(self.find_element(*self.custom_iframe))
        self.find_element(*self.custom_submit_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_id_loc)
        # # 每页显示多少条
        # self.find_element(*self.page_any_loc).send_keys("1")
        # self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        sleep(0.5)
        # 每页显示多少条
        self.find_element(*self.page_any_loc).send_keys("1")
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        # # 输入查询用户
        # ActionChains(self.driver).move_to_element(self.find_element(*self.called_user_loc)).perform()
        # sleep(1)
        # self.find_element(*self.called_user_loc).click()
        # self.find_element(*self.called_user_box_loc).send_keys(called_user)
        # self.find_element(*self.called_user_box_loc).send_keys(Keys.ENTER)
        # sleep(1)
        # ActionChains(self.driver).move_to_element(self.find_element(*self.session_type_loc)).perform()




    def paging_verify(self):
        #验证分页查询每页显示数量
        self.designate_time_called()
        num = self.find_elements(*(By.CLASS_NAME, 'contentbody'))
        return str(len(num))



    def custom_time_verify_0(self):
        #自定义时间查询所有告警数量
        self.designate_time_called()
        s = self.query_num()
        return s

    def custom_time_verify_1(self):
        #自定义时间查询告警等级为严重的数量
        self.designate_time_called()
        self.find_element(*self.alarm_level_loc).click()
        self.find_element(*self.alarm_level_serious).click()
        s = self.query_num()
        return s

    def custom_time_verify_2(self):
        #自定义时间查询告警等级为一般的数量
        self.designate_time_called()
        self.find_element(*self.alarm_level_loc).click()
        self.find_element(*self.alarm_level_generic).click()
        s = self.query_num()
        return s

    def custom_time_verify_3(self):
        #自定义时间查询告警等级为轻微的数量
        self.designate_time_called()
        self.find_element(*self.alarm_level_loc).click()
        self.find_element(*self.alarm_level_slight).click()
        s = self.query_num()
        return s


    def network_event_log(self):
        #进入网络事件日志页面
        self.come_iframe_comm()
        self.find_element(*(By.LINK_TEXT, '网络事件日志')).click()
        # sleep(10)
        s = self.find_element(*(By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[5]')).text
        print(s)
        return s
