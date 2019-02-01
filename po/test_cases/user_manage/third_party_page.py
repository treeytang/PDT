from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class ThirdParty(Page):
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
    # 第三方用户定位
    third_party_user = (By.LINK_TEXT, '第三方用户')
    # 嵌套页面定位
    iframe_loc = 'mainFrame'
    #显示数量element定位
    show_num_loc = (By.XPATH, '//*[@id="thirdPartyUserList"]/tr')
    #每页显示数量输入框定位
    page_show_num_loc = (By.XPATH, '//*[@id="freestyle"]/div/div/div/div[2]/div[1]/div[5]/input')


    def come_iframe_page(self):
        #进入iframe页面公用函数定位
        self.find_element(*self.user_manage_loc).click()
        self.find_element(*self.third_party_user).click()
        self.switch_frame(self.iframe_loc)

    def page_show_num(self):
        #显示数量验证
        self.come_iframe_page()
        elements = self.find_elements(*self.show_num_loc)
        return str(len(elements))

    def paging_verify(self):
        #分页验证
        self.come_iframe_page()
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        sleep(3)
        self.send_keys('1', *self.page_show_num_loc)
        self.send_enter(*self.page_show_num_loc)
        sleep(3)
        elements = self.find_elements(*self.show_num_loc)
        return str(len(elements))


    #用户添加定位
    user_add_loc = (By.LINK_TEXT, '用户添加')
    #号码定位
    number_loc = (By.ID, 'number')
    #空中实名制别名
    alias_loc = (By.ID, 'alias')
    #警号定位
    policeId_loc = (By.ID, 'policeId')
    #保存定位
    save_loc = (By.ID, 'btnSubmit')


    def add_user(self):
        #用户添加
        self.come_iframe_page()
        self.find_element(*self.user_add_loc).click()
        self.send_keys('88888888', *self.number_loc)
        self.send_keys('成都测试', *self.alias_loc)
        self.find_element(*self.save_loc).click()
        sleep(1)
        element = self.find_element(*(By.LINK_TEXT, '888-88-888'))
        if element:
            return True
        return False

    def add_user_1(self):
        #用户添加
        self.come_iframe_page()
        self.find_element(*self.user_add_loc).click()
        self.send_keys('aaaaaa', *self.number_loc)
        self.send_keys('成都测试', *self.alias_loc)
        self.find_element(*self.save_loc).click()
        sleep(1)
        element = self.find_element(*(By.LINK_TEXT, 'aaaaaa'))
        if element:
            return False
        return True

    def add_user_2(self):
        #用户添加
        self.come_iframe_page()
        self.find_element(*self.user_add_loc).click()
        self.send_keys('400aa00', *self.number_loc)
        self.send_keys('成都测试', *self.alias_loc)
        self.find_element(*self.save_loc).click()
        sleep(1)
        element = self.find_element(*(By.LINK_TEXT, 'aaaaaa'))
        if element:
            return False
        return True

    def add_user_3(self):
        #用户添加
        self.come_iframe_page()
        self.find_element(*self.user_add_loc).click()
        self.send_keys('成都测试', *self.number_loc)
        self.send_keys('成都测试', *self.alias_loc)
        self.find_element(*self.save_loc).click()
        sleep(1)
        element = self.find_element(*(By.LINK_TEXT, 'aaaaaa'))
        if element:
            return False
        return True

    def add_user_4(self):
        #用户添加
        self.come_iframe_page()
        self.find_element(*self.user_add_loc).click()
        self.send_keys('@#$%^&', *self.number_loc)
        self.send_keys('成都测试', *self.alias_loc)
        self.find_element(*self.save_loc).click()
        sleep(1)
        element = self.find_element(*(By.LINK_TEXT, 'aaaaaa'))
        if element:
            return False
        return True

    def add_user_5(self):
        #用户添加
        self.come_iframe_page()
        self.find_element(*self.user_add_loc).click()
        self.send_keys('88888888', *self.number_loc)
        self.send_keys('成都测试', *self.alias_loc)
        self.find_element(*self.save_loc).click()
        if self.find_element(*(By.LINK_TEXT, '888-88-888')):
            return False
        return True



    def del_user(self):
        #删除用户
        self.come_iframe_page()
        self.find_element(*(By.XPATH, '//*[@id="thirdPartyUserList"]/tr[17]/td[9]/button'))
        element = self.find_element(*(By.LINK_TEXT, '888-88-888'))
        if element:
            return False
        return True