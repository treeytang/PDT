from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class Mobile_Station(Page):
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


    #用户管理定位
    user_manage_loc = (By.XPATH, '//*[@id="menu69"]/div[1]/a')
    #移动台管理定位
    MS_manage_loc = (By.LINK_TEXT, '移动台管理')
    #嵌套页面定位
    iframe_loc = 'mainFrame'

    #页面显示列表手台信息定位
    mobile_msg_loc = (By.XPATH, '//*[@id="muserList"]/tr')
    #每页显示数量定位
    page_show_num_loc = (By.XPATH, '//*[@id="freestyle"]/div/div/div[1]/div[2]/div[2]/div[5]/input')
    #电子序列号搜索定位
    serial_query_loc = (By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/th[12]')
    #电子序列号搜索输入框定位
    serial_query_input_loc = (By.ID, 'esn')
    #删除定位
    del_loc = (By.XPATH, '//*[@id="muserList"]/tr/td[14]/button[5]')
    # 删除确定按钮
    del_ensure = (By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[1]')



    #开户按钮定位
    add_icon_loc = (By.ID, 'add')
    #号码范围 区号定位
    area_code_loc = (By.XPATH, '//*[@id="ssi"]/div[3]/span[1]/input')
    #队号定位
    team_code_loc = (By.XPATH, '//*[@id="ssi"]/div[3]/span[4]/input')
    #个号定位
    individual_code_loc = (By.XPATH, '//*[@id="ssi"]/div[3]/span[6]/input')
    #无效号码定位
    nullty_num_loc = (By.ID, 'tip_ssi')
    #优先级下拉选择框定位
    th_box_select_loc = (By.XPATH, '//*[@id="priority"]/div/select')
    # VPN下拉选择框
    VPN_loc = (By.XPATH, '//*[@id="vpn_index"]/div/select')
    #电子序列号输入框定位
    serial_num = (By.ID, 'esn')
    #审批覆盖取消按钮定位
    cancel_btn_loc = (By.ID, 'no')
    #审批覆盖提示窗口定位
    alert_loc = (By.XPATH, '/html/body/div[3]/div[1]')


    #实名制信息定位
    real_name_loc = (By.XPATH, '//*[@id="freestyle"]/div[1]/div[2]/div/div[2]/div[1]')
    #厂商定位
    manufacturer_loc = (By.ID, 'manufacturer')
    # 性别定位
    sex_loc = (By.ID, 'sex')
    #警种定位
    police_type_loc = (By.ID, 'policeType')
    #职位定位
    position_loc = (By.ID, 'position')




    # 确定按钮定位
    add_loc = (By.ID, 'add')





    def come_iframe_page(self):
        #进入嵌套页面公用函数
        self.find_element(*self.user_manage_loc).click()
        self.find_element(*self.MS_manage_loc).click()
        self.switch_frame(self.iframe_loc)

    def come_iframe_verify(self):
        #进入嵌套页面验证
        self.come_iframe_page()
        msg = self.find_element(*(By.LINK_TEXT, '移动用户列表')).text
        return msg

    def query_num_verify(self):
        #显示手台数量验证
        self.come_iframe_page()
        self.find_element(*self.page_show_num_loc).clear()
        self.find_element(*self.page_show_num_loc).send_keys('1000')
        self.send_enter(*self.page_show_num_loc)
        sleep(3)
        elements = self.find_elements(*self.mobile_msg_loc)
        return str(len(elements))

    def come_add_icon(self):
        #进入开户页面验证
        self.come_iframe_page()
        self.find_element(*self.add_icon_loc).click()
        msg = self.find_element(*(By.XPATH, '//*[@id="freestyle"]/div[1]/div[1]/div/div[1]/span')).text
        return msg

    '''
        进入开户界面进行测试
        1.号码范围的取值：区号328--806   队号20--41  个号200--899 各个分别提取边界值进行验证
        2.空中实名制别名：默认为个号 场景法 不填写 填写大于7位（当大于7位时 前段默认会删除第七位后的其它字符）
        3.通话限时 场景法 
        4.
    '''

    def basic_msg(self, area_num, team_num, individual_num, first_num='0', serial_num=None, value='300'):
        #进入开户页 填写基本信息
        self.come_iframe_page()
        self.find_element(*self.add_icon_loc).click()
        self.find_element(*self.area_code_loc).send_keys(area_num)
        self.find_element(*self.team_code_loc).send_keys(team_num)
        self.find_element(*self.individual_code_loc).send_keys(individual_num)
        self.select(*self.th_box_select_loc).select_by_value(first_num)
        self.send_keys(*(By.ID, 'session_timer'), value=value)
        self.find_element(*self.serial_num).send_keys(serial_num)

    def real_name_system(self, text='海格恒通', gender='女', policeType='交警', position='二级警员'):
        #公用函数
        l = []
        #开户界面 填写实名制信息
        self.find_element(*self.real_name_loc).click()
        #厂商信息
        self.select(*self.manufacturer_loc).select_by_visible_text(text)
        msg = self.find_element(*(By.XPATH, '//*[@id="inputForm"]/div/table/tbody/tr[2]/td[2]/div/div/span[1]')).text
        #性别信息
        self.select(*self.sex_loc).select_by_visible_text(gender)
        msg_1 = self.find_element(*(By.XPATH, '//*[@id="inputForm"]/div/table/tbody/tr[3]/td[2]/div/div/span[1]')).text
        #警种信息
        self.select(*self.police_type_loc).select_by_visible_text(policeType)
        msg_2 = self.find_element(*(By.XPATH, '//*[@id="inputForm"]/div/table/tbody/tr[5]/td[2]/div/div/span[1]')).text
        #职位信息
        self.select(*self.position_loc).select_by_visible_text(position)
        msg_3 = self.find_element(*(By.XPATH, '//*[@id="inputForm"]/div/table/tbody/tr[6]/td[2]/div/div/span[1]')).text
        l.append(msg)
        l.append(msg_1)
        l.append(msg_2)
        l.append(msg_3)
        return l

    def query_del(self, num):
        #公用函数 用于添加后进行删除
        self.find_element(*self.serial_query_loc).click()
        self.find_element(*self.serial_query_input_loc).send_keys(num)
        self.send_enter(*self.serial_query_input_loc)
        sleep(2)
        element = self.find_elements(*self.mobile_msg_loc)
        self.find_element(*self.del_loc).click()
        self.switch_to_default()
        self.find_element(*self.del_ensure).click()
        return element


    def add_icon_1(self):
        #进入开户界面 只填写基本信息 验证 未注册的正确基本信息
        self.basic_msg('800', '41', '300', first_num='1', serial_num='555555555555555', value='300')
        self.find_element(*self.add_loc).click()
        sleep(4)
        element = self.query_del('555555555555555')
        if len(element) == 1:
            return '添加成功'
        return 'Fail'

    def add_icon_1_1(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 区号最小值减一 327
        self.basic_msg('327', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return True
        return False

    def add_icon_1_2(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 区号最大值加一 807  区号328--806   队号20--41  个号200--899
        self.basic_msg('807', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return True
        return False

    def add_icon_1_3(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 输入英文：aa  区号328--806   队号20--89  个号200--899
        self.basic_msg('aa', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return True
        return False

    def add_icon_1_4(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 输入中文：警察  区号328--806   队号20--41  个号200--899
        self.basic_msg('警察', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return True
        return False

    def add_icon_1_5(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的队号 最大值加一：42
        self.basic_msg('800', '90', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        sleep(5)
        if msg == '无效号码':
            return True
        return False

    def add_icon_1_6(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的队号 最小值减一：19
        self.basic_msg('800', '19', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return True
        return False


    def add_icon_2(self):
        # 进入开户界面 只填写基本信息 验证 已注册的正确基本信息
        self.basic_msg('328', '21', '203', first_num='0', serial_num='555555555555555', value='300')
        self.find_element(*self.add_loc).click()
        msg = self.find_element(*self.alert_loc).text
        self.find_element(*self.cancel_btn_loc).click()
        if msg == '以下号码已通过实名制审批，需要覆盖吗？':
            return True
        return False

    def add_icon_3(self):
        #进入开户界面 先填写基本信息再填写实名制信息 验证 实名制信息相关选择(边界值 全选第一个)
        self.basic_msg('800', '41', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.real_name_system(text='海格恒通', gender='女', policeType='交警', position='二级警员')
        self.find_element(*self.add_loc).click()
        self.query_del('555555555555555')
        return msg

    def add_icon_4(self):
        #进入开户界面 先填写基本信息再填写实名制信息 验证 实名制信息相关选择(边界值 全选最后一个个)
        self.basic_msg('800', '41', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.real_name_system(text='科立讯', gender='男', policeType='巡警', position='总警监')
        self.find_element(*self.add_loc).click()
        self.query_del('555555555555555')
        return msg

