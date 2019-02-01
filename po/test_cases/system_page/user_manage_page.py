from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class User_manage(Page):
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
    #用户管理定位
    user_manage_loc = (By.XPATH, '//*[@id="menu2"]/div[2]/ul/li[1]/a')
    #嵌套页面定位
    iframe_loc = 'mainFrame'

    #列表显示用户数量
    user_nums = (By.XPATH, '//*[@id="contentTable"]/tbody/tr')

    #登录名查询输入框
    login_name_input = (By.ID, 'loginName')
    #姓名查询输入框
    name_input = (By.ID, 'name')

    def come_iframe_page(self):
        #进入嵌套页面
        self.find_element(*self.sys_manage_loc).click()
        self.find_element(*self.user_manage_loc).click()
        self.switch_frame(self.iframe_loc)

    def come_page_verify(self):
        #进入页面验证
        self.come_iframe_page()
        element1 = WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT,'用户列表')))
        element2 = WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT,'用户添加')))
        if element1 and element2:
            return True
        else:
            return False

    def query_user_num(self):
        #页面显示用户数量验证
        self.come_iframe_page()
        elements = self.find_elements(*self.user_nums)
        print(len(elements))
        return str(len(elements))

    def input_query_1(self):
        #通过登录名模糊查询 查询登录名中含有w的用户
        self.come_iframe_page()
        self.find_element(*self.login_name_input).send_keys('w')
        self.send_enter(*self.login_name_input)
        elements = self.find_elements(*self.user_nums)
        print(len(elements))
        return str(len(elements))

    def input_query_2(self):
        #通过登录名模糊查询 查询姓名中含有h的用户
        self.come_iframe_page()
        self.find_element(*self.name_input).send_keys('测试')
        self.send_enter(*self.name_input)
        elements = self.find_elements(*self.user_nums)
        print(len(elements))
        return str(len(elements))

    def add_user(self):
        #添加用户
        self.come_iframe_page()
        #进入用户添加界面进行操作
        self.find_element(*(By.LINK_TEXT, '用户添加')).click()
        self.find_element(*(By.ID, 'no')).send_keys('007')
        self.find_element(*(By.ID, 'name')).send_keys('测试007')
        self.find_element(*(By.ID, 'loginName')).send_keys('007')
        self.find_element(*(By.ID, 'newPassword')).send_keys('admin')
        self.find_element(*(By.ID, 'confirmNewPassword')).send_keys('admin')
        self.find_element(*(By.ID, 'btnSubmit')).click()
        #查找出添加的用户是否存在
        self.find_element(*self.name_input).send_keys('测试007')
        self.send_enter(*self.name_input)
        element = self.find_element(*(By.XPATH, '//*[@id="contentTable"]/tbody/tr/td[1]')).text
        self.find_element(*(By.XPATH, '//*[@id="contentTable"]/tbody/tr/td[8]/a[2]')).click()
        self.switch_to_default()
        self.find_element(*(By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[1]')).click()
        print(element)
        if element:
            return True
        return False