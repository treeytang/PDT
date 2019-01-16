from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class DRM_User(Page):
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

    # 用户管理定位
    user_manage_loc = (By.XPATH, '//*[@id="menu69"]/div[1]/a')
    # 移动台管理定位
    DMR_user_loc = (By.LINK_TEXT, 'DMR用户')
    # 嵌套页面定位
    iframe_loc = 'mainFrame'


    #每页显示数量输入框定位
    page_show_num = (By.XPATH, '//*[@id="freestyle"]/div/div[2]/div/div[5]/input')
    #页面显示数量element定位
    user_show_num = (By.XPATH, '//*[@id="freestyle"]/div/div[2]/table/tbody/tr')

    def come_iframe_page(self):
        #进入嵌套页面 默认进入DMR用户页面
        self.find_element(*self.user_manage_loc).click()
        self.find_element(*self.DMR_user_loc).click()
        self.switch_frame(self.iframe_loc)

    def user_verity(self):
        #验证页面显示数量
        self.come_iframe_page()
        self.send_keys('100',*self.page_show_num)
        self.send_enter(*self.page_show_num)
        sleep(1)
        elements = self.find_elements(*self.user_show_num)
        return str(len(elements))
