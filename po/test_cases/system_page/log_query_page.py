from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep
import re



class Log_Query(Page):
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
        sleep(1)


    #系统管理定位
    sys_manage_loc = (By.XPATH, '//*[@id="menu2"]/div[1]/a')
    #日志查询定位
    log_query_loc = (By.XPATH, '//*[@id="menu2"]/div[2]/ul/li[4]/a')
    #嵌套页面定位
    iframe_loc = 'mainFrame'

    #嵌套页面验证
    iframe_verify_loc = (By.LINK_TEXT, '日志查询')

    #开始时间框定位
    begin_date_loc = (By.ID, 'beginDate')
    #时间iframe定位
    begin_date_iframe_loc = (By.XPATH, '/html/body/div[2]/iframe')
    #月定位
    month_loc = (By.XPATH, '//*[@id="dpTitle"]/div[3]/input')
    #年定位
    year_loc = (By.XPATH, '//*[@id="dpTitle"]/div[4]/input')
    #确定按钮
    ensure_loc = (By.ID, 'dpOkInput')

    #结束时间框定位
    end_date_loc = (By.ID, 'endDate')
    #iframe定位
    end_date_iframe_loc = (By.XPATH, '/html/body/div[2]/iframe')

    #查询按钮定位
    query_btn_loc = (By.ID, 'btnSubmit')

    #查询数量定位
    query_num_loc = (By.XPATH, '//*[@id="freestyle"]/div/div[2]/div/ul')

    #操作目标输入框定位
    title_loc = (By.ID, 'title')

    #URL输入框定位
    URL_loc = (By.ID, 'requestUri')



    def come_iframe_page(self):
        #公用函数  进入嵌套页面
        self.find_element(*self.sys_manage_loc).click()
        self.find_element(*self.log_query_loc).click()
        self.switch_frame(self.iframe_loc)

    def come_iframe_verify(self):
        #是否进入页面验证
        self.come_iframe_page()
        msg = self.find_element(*self.iframe_verify_loc).text
        return msg

    def verify_log_num(self):
        #验证日志显示数量
        self.come_iframe_page()
        self.find_element(*self.begin_date_loc).click()
        self.switch_to_default()
        xf = self.find_element(*self.begin_date_iframe_loc)
        self.switch_frame(xf)
        self.find_element(*self.month_loc).clear()
        #开始时间见框的月
        self.find_element(*self.month_loc).send_keys('3')
        self.find_element(*self.year_loc).clear()
        self.find_element(*self.year_loc).send_keys('2019')
        self.find_element(*self.ensure_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_loc)
        self.find_element(*self.end_date_loc).click()
        self.switch_to_default()
        xf = self.find_element(*self.end_date_iframe_loc)
        self.switch_frame(xf)
        self.find_element(*self.month_loc).clear()
        self.find_element(*self.month_loc).send_keys('4')
        self.find_element(*self.year_loc).clear()
        self.find_element(*self.year_loc).send_keys('2019')
        self.find_element(*self.ensure_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_loc)
        self.find_element(*self.query_btn_loc).click()
        a = self.find_element(*self.query_num_loc).text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d', a))
        return s

    def verify_log_num_1(self):
        #验证操作目标为System Login日志显示数量
        self.come_iframe_page()
        self.find_element(*self.title_loc).send_keys('System Login')
        self.find_element(*self.begin_date_loc).click()
        self.switch_to_default()
        xf = self.find_element(*self.begin_date_iframe_loc)
        self.switch_frame(xf)
        self.find_element(*self.month_loc).clear()
        self.find_element(*self.month_loc).send_keys('3')
        self.find_element(*self.year_loc).clear()
        self.find_element(*self.year_loc).send_keys('2019')
        self.find_element(*self.ensure_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_loc)
        self.find_element(*self.end_date_loc).click()
        self.switch_to_default()
        xf = self.find_element(*self.end_date_iframe_loc)
        self.switch_frame(xf)
        self.find_element(*self.month_loc).clear()
        self.find_element(*self.month_loc).send_keys('4')
        self.find_element(*self.year_loc).clear()
        self.find_element(*self.year_loc).send_keys('2019')
        self.find_element(*self.ensure_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_loc)
        self.find_element(*self.query_btn_loc).click()
        a = self.find_element(*self.query_num_loc).text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d', a))
        return s


    def verify_log_num_2(self):
        #验证url为/nmp/sys/user/list日志显示数量
        self.come_iframe_page()
        self.find_element(*self.URL_loc).send_keys('/nmp/sys/user/list')
        self.find_element(*self.begin_date_loc).click()
        self.switch_to_default()
        xf = self.find_element(*self.begin_date_iframe_loc)
        self.switch_frame(xf)
        self.find_element(*self.month_loc).clear()
        self.find_element(*self.month_loc).send_keys('3')
        self.find_element(*self.year_loc).clear()
        self.find_element(*self.year_loc).send_keys('2019')
        self.find_element(*self.ensure_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_loc)
        self.find_element(*self.end_date_loc).click()
        self.switch_to_default()
        xf = self.find_element(*self.end_date_iframe_loc)
        self.switch_frame(xf)
        self.find_element(*self.month_loc).clear()
        self.find_element(*self.month_loc).send_keys('4')
        self.find_element(*self.year_loc).clear()
        self.find_element(*self.year_loc).send_keys('2019')
        self.find_element(*self.ensure_loc).click()
        self.switch_to_default()
        self.switch_frame(self.iframe_loc)
        self.find_element(*self.query_btn_loc).click()
        a = self.find_element(*self.query_num_loc).text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d', a))
        return s
