from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class User_Office(Page):
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
    system_manage = (By.XPATH, '//*[@id="menu2"]/div[1]/a')
    #用户单位定位
    user_office = (By.XPATH, '//*[@id="menu2"]/div[2]/ul/li[2]/a')
    #进入到嵌套表单定位
    office_iframe_id = 'mainFrame'



    #单位添加定位
    office_add = (By.XPATH, '//*[@id="freestyle"]/div/div[1]/ul/li[2]/a')
    #上级单位选择框定位
    choice_head_office = (By.ID, 'officeName')
    #嵌套页面定位
    iframe_select = 'layui-layer-iframe1'
    #上级单位选择勾选框
    checkbox_select_office = (By.XPATH, '//*[@id="57ae08edeb2041c09c68aee41975724b"]/td[2]/label')
    #单位选择确定按钮
    choice_ensure = (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]')
    #单位名称 区域 定位
    office_area_name = (By.ID, 'areaName')
    #单位名称 机构 定位
    organization_name = (By.ID, 'name')
    #单位编码定位
    office_code = (By.ID, 'code')
    #保存定位
    save_loc = (By.ID, 'btnSubmit')





    #添加下级单位定位
    head_add_next_office = (By.XPATH, '//*[@id="1"]/td[9]/a[3]')




    #进入系统管理，用户单位页面
    def come_office_manage(self):
        self.find_element(*self.system_manage).click()
        self.find_element(*self.user_office).click()
        self.switch_frame(self.office_iframe_id)





    #验证进入进入用户单位页面
    def come_user_office_verify(self):
        self.come_office_manage()
        verify = self.find_element(*(By.LINK_TEXT, "省公安厅")).text
        return verify

    #单位添加测试 循环添加10个有效单位
    def office_add_verify(self):
        self.come_office_manage()
        add_list = []
        for i in range(10):
            self.find_element(*self.office_add).click()
            self.find_element(*self.choice_head_office).click()
            self.find_element(*self.choice_ensure).click()
            s = '测试' + str(i)
            self.find_element(*self.office_area_name).send_keys(s)
            self.find_element(*self.organization_name).send_keys('成都')
            self.find_element(*self.office_code).send_keys('111111111111')
            self.find_element(*self.save_loc).click()
            sleep(1)
            s1 = s+'成都'
            msg = self.find_element(*(By.LINK_TEXT, s1)).text
            if msg:
                add_list.append(msg)
        print(len(add_list))
        print(len(self.find_elements(*(By.LINK_TEXT, '111111111111'))))
        return str(len(add_list))



    #单位删除测试 循环删除 10 个单位
    def office_del_verify(self):
        self.come_office_manage()
        del_list = self.find_elements(*(By.LINK_TEXT, '删除'))
        print("共有%d条记录"%(len(del_list)))
        i = 0
        while True:
            if i > (len(del_list)-1):
                print("共执行了%d次"%i)
                break
            # del_btn.click()
            self.find_element(*(By.LINK_TEXT, '删除')).click()
            self.switch_to_default()
            self.find_element(*(By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[1]')).click()
            self.switch_frame(self.office_iframe_id)
            i+=1

        length = len(self.find_elements(*(By.LINK_TEXT, '删除')))
        # element = WebDriverWait(self.driver, 5, 0.5).until(
        #     EC.presence_of_all_elements_located((By.LINK_TEXT, "删除"))
        # )
        if length>0:
            return False
        else:
            return True


    def head_add_next_office_verify(self):
        self.come_office_manage()
        add_list = []
        for i in range(10, 20):
            self.find_element(*self.head_add_next_office).click()
            self.find_element(*self.choice_head_office).click()
            self.find_element(*self.choice_ensure).click()
            s = '测试' + str(i)
            self.find_element(*self.office_area_name).send_keys(s)
            self.find_element(*self.organization_name).send_keys('成都')
            self.find_element(*self.office_code).send_keys('111111111111')
            self.find_element(*self.save_loc).click()
            sleep(1)
            s1 = s+'成都'
            msg = self.find_element(*(By.LINK_TEXT, s1)).text
            if msg:
                add_list.append(msg)
        num = len(self.find_elements(*(By.XPATH, '//*[@id="treeTableList"]/tr')))-1
        print(num)
        print(len(add_list))
        return str(num)


    def add_show_verify(self):
        self.come_office_manage()
        self.find_element(*self.office_add).click()
        self.find_element(*self.choice_head_office).click()
        self.find_element(*self.choice_ensure).click()
        s = '测试'
        self.find_element(*self.office_area_name).send_keys(s)
        self.find_element(*self.organization_name).send_keys('成都')
        self.find_element(*self.office_code).send_keys('111111111111')
        self.find_element(*self.save_loc).click()
        verify = self.find_element(*(By.LINK_TEXT, "测试成都")).text
        return verify
