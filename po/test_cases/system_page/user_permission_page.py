from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class User_permission(Page):
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
    #用户权限定位
    user_permission_loc = (By.XPATH, '//*[@id="menu2"]/div[2]/ul/li[3]/a')
    #嵌套页面定位
    iframe_loc = 'mainFrame'

    #嵌套页面验证
    iframe_verify_loc = (By.LINK_TEXT, '权限列表')

    #列表显示用户数量
    user_nums = (By.XPATH, '//*[@id="contentTable"]/tbody/tr')

    #权限添加定位
    add_permission_loc = (By.LINK_TEXT, '权限添加')
    #权限名称输入框定位
    permission_name_loc = (By.ID, 'name')
    #英文名输入框定位
    english_name_loc = (By.ID, 'enname')
    #复选框功能菜单定位
    check_box_loc = (By.ID, 'menuTree_1_check')
    #保存按钮定位
    save_btn_loc = (By.ID, 'btnSubmit')

    def come_iframe_page(self):
        #进入嵌套页面
        self.find_element(*self.sys_manage_loc).click()
        self.find_element(*self.user_permission_loc).click()
        self.switch_frame(self.iframe_loc)

    def come_iframe_verify(self):
        self.come_iframe_page()
        msg = self.find_element(*self.iframe_verify_loc).text
        return msg

    def verify_user_num(self):
        self.come_iframe_page()
        elements = self.find_elements(*self.user_nums)
        num = str(len(elements)-1)
        return num

    def add_permission(self):
        self.come_iframe_page()
        self.find_element(*self.add_permission_loc).click()
        self.find_element(*self.permission_name_loc).send_keys('自动化测试')
        self.find_element(*self.english_name_loc).send_keys('auto_test')
        self.find_element(*self.check_box_loc).click()
        self.find_element(*self.save_btn_loc).click()
        element = self.find_element(*(By.LINK_TEXT, '自动化测试')).text
        self.find_element(*(By.XPATH, '//*[@id="contentTable"]/tbody/tr[5]/td[3]/a[2]')).click()
        self.switch_to_default()
        self.find_element(*(By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[1]')).click()
        return element

    def modify_permission(self):
        self.come_iframe_page()
        self.find_element(*self.add_permission_loc).click()
        self.find_element(*self.permission_name_loc).send_keys('自动化测试')
        self.find_element(*self.english_name_loc).send_keys('auto_test')
        self.find_element(*self.check_box_loc).click()
        self.find_element(*self.save_btn_loc).click()
        self.find_element(*(By.LINK_TEXT, '自动化测试')).click()
        self.find_element(*(By.ID, 'menuTree_4_check')).click()
        self.find_element(*self.save_btn_loc).click()
        self.find_element(*(By.LINK_TEXT, '自动化测试')).click()
        element = self.find_element(*(By.ID, 'menuTree_4_check')).get_attribute('class')
        # js = "var q=document.documentElement.scrollTop=1000000"
        # self.script(js)
        self.find_element(*(By.ID, 'btnSubmit')).click()
        # sleep(1)
        self.find_element(*(By.XPATH, '//*[@id="contentTable"]/tbody/tr[5]/td[3]/a[2]')).click()
        self.switch_to_default()
        self.find_element(*(By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[1]')).click()
        if element == 'button chk checkbox_false_full':
            return True
        return False