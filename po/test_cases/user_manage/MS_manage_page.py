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
    #矩阵显示模式按钮定位
    show_matrix_loc = (By.ID, 'togglePage')


    #用户映射定位
    user_map_loc = (By.LINK_TEXT, '用户映射')
    #列表显示数量定位
    map_show_num = (By.XPATH, '//*[@id="relate"]/tr')
    #每页显示数量输入框定位
    page_num_loc = (By.XPATH, '//*[@id="freestyle"]/div/div[2]/div[2]/div[1]/div[5]/input')
    #用户号码范围 区号输入框
    map_area_loc = (By.XPATH, '//*[@id="phone1"]/div[2]/span[1]/input')
    #用户号码范围 队号输入框
    map_team_loc = (By.XPATH, '//*[@id="qh"]/input')
    #用户号码范围 个号输入框
    map_individual_loc_1 = (By.XPATH, '//*[@id="phone1"]/div[2]/span[5]/input')
    map_individual_loc_2 = (By.XPATH, '//*[@id="phone1"]/div[2]/span[7]/input')
    # PDT用户号码范围 区号输入框
    PDT_area_loc = (By.XPATH, '//*[@id="phone2"]/div[2]/span[1]/input')
    # PDT用户号码范围 队号输入框
    PDT_team_loc = (By.XPATH, '//*[@id="phone2"]/div[2]/span[3]/input')
    # PDT用户号码范围 个号输入框
    PDT_individual_loc_1 = (By.XPATH, '//*[@id="phone2"]/div[2]/span[5]/input')
    PDT_individual_loc_2 = (By.XPATH, '//*[@id="phone2"]/div[2]/span[7]/input')
    #添加按钮定位
    map_add_btn_loc = (By.ID, 'add')
    #所有删除操作按钮定位
    map_del_btn_loc = (By.XPATH, '//*[@id="relate"]/tr/td[10]/button')
    #提示弹窗定位
    map_alert_loc = (By.XPATH, '/html/body/div[2]')

    #本地在线用户定位
    local_online_user_loc = (By.XPATH, '//*[@id="m_class"]/li[3]/a')
    #列表数量定位
    LOU_show_num = (By.XPATH, '//*[@id="regUserList"]/tr')
    #每页显示数量输入框定位
    LOU_input_loc = (By.XPATH, '//*[@id="freestyle"]/div/div[2]/div/div[5]/input')







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
        1.号码范围的取值：区号328--806   队号20--89  个号200--899 各个分别提取边界值进行验证
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
        self.send_keys(value, *(By.ID, 'session_timer'))
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
            return "pass"
        return 'fail'

    def add_icon_1_1(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 区号最小值减一 327
        self.basic_msg('327', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return "pass"
        return "fail"

    def add_icon_1_2(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 区号最大值加一 807  区号328--806   队号20--89  个号200--899
        self.basic_msg('807', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return "pass"
        return "fail"

    def add_icon_1_3(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 输入英文：aa  区号328--806   队号20--89  个号200--899
        self.basic_msg('aa', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return "pass"
        return "fail"

    def add_icon_1_4(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 输入中文：警察  区号328--806   队号20--89  个号200--899
        self.basic_msg('警察', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return "pass"
        return "fail"

    def add_icon_1_7(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 4位区号  区号328--806   队号20--89  个号200--899
        self.basic_msg('3333', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        sleep(5)
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return "pass"
        return "fail"

    def add_icon_1_8(self):
        #进入开户界面 只填写基本信息 验证 号码范围 错误的区号 2位区号  区号328--806   队号20--89  个号200--899
        self.basic_msg('44', '20', '410', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg=='无效号码':
            return "pass"
        return "fail"


    def add_icon_1_5(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的队号 最大值加一：90
        self.basic_msg('800', '90', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        sleep(5)
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_6(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的队号 最小值减一：19
        self.basic_msg('800', '19', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_9(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的队号 输入英文:aa
        self.basic_msg('800', 'aa', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_10(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的队号 输入中文:警察
        self.basic_msg('800', '警察', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_11(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的个号 最大值加一：900
        self.basic_msg('800', '23', '900', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_12(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的个号 最小值减一：199
        self.basic_msg('800', '23', '199', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_13(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的个号 输入英文:aaa
        self.basic_msg('800', '23', 'aaa', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_1_14(self):
        #进入开户界面 只填写基本信息 验证 号码的范围 错误的个号 输入中文:一二三
        self.basic_msg('800', '23', '一二三', first_num='1', serial_num='555555555555555', value='300')
        msg = self.find_element(*self.nullty_num_loc).text
        if msg == '无效号码':
            return "pass"
        return "fail"

    def add_icon_2(self):
        # 进入开户界面 只填写基本信息 验证 已注册的正确基本信息
        self.basic_msg('445', '30', '214', first_num='0', serial_num='555555555555555', value='300')
        self.find_element(*self.add_loc).click()
        msg = self.find_element(*self.alert_loc).text
        self.find_element(*self.cancel_btn_loc).click()
        if msg == '以下号码已通过实名制审批，需要覆盖吗？':
            return "pass"
        return "fail"

    def add_icon_3(self):
        #进入开户界面 先填写基本信息再填写实名制信息 验证 实名制信息相关选择(边界值 全选第一个)
        self.basic_msg('800', '41', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.real_name_system(text='海格恒通', gender='女', policeType='交警', position='二级警员')
        self.find_element(*self.add_loc).click()
        self.query_del('555555555555555')
        if msg == ['海格恒通', '女', '交警', '二级警员']:
            return "pass"
        return "fail"

    def add_icon_4(self):
        #进入开户界面 先填写基本信息再填写实名制信息 验证 实名制信息相关选择(边界值 全选最后一个个)
        self.basic_msg('800', '41', '300', first_num='1', serial_num='555555555555555', value='300')
        msg = self.real_name_system(text='科立讯', gender='男', policeType='巡警', position='总警监')
        self.find_element(*self.add_loc).click()
        self.query_del('555555555555555')
        if msg==['科立讯', '男', '巡警', '总警监']:
            return "pass"
        return "fail"

    def show_matrix(self):
        #进入矩阵显示模式页面
        self.come_iframe_page()
        self.find_element(*self.show_matrix_loc).click()
        msg = self.find_element(*(By.ID, 'togglePage')).text
        if msg == '切换至列表显示模式':
            return True
        return False




    #移动台管理  --------用户映射




    def user_map_show_num(self):
        #进入用户映射页面 验证显示数量
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        elements = self.find_elements(*self.map_show_num)
        return str(len(elements))

    def user_map_show_num_1(self):
        #进入用户映射页面 验证分页显示显示数量
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('1', *self.page_num_loc)
        self.send_enter(*self.page_num_loc)
        sleep(1)
        elements = self.find_elements(*self.map_show_num)
        return str(len(elements))


    def del_(self):
        #用户映射界面公用删除函数
        elements = self.find_elements(*self.map_del_btn_loc)
        if len(elements)!=5:
            return False
        elements.pop().click()
        sleep(2)
        self.switch_to_default()
        self.find_element(*self.del_ensure).click()


    def user_map_show_num_2(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 800 41 200/210  800 41 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('800', *self.map_area_loc)
        self.send_keys('41', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('800', *self.PDT_area_loc)
        self.send_keys('41', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        self.find_element(*self.map_add_btn_loc).click()
        element = self.find_element(*(By.LINK_TEXT, '800-41-200'))
        self.del_()
        if element:
            return True
        return False

    def user_map_show_num_2_1(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的区号 区号最小值减一：327 327 41 200/210  327 41 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('327', *self.map_area_loc)
        self.send_keys('41', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('327', *self.PDT_area_loc)
        self.send_keys('41', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        # element = self.find_element(*(By.LINK_TEXT, '800-41-200'))
        # self.del_()
        if element:
            return False
        return True

    def user_map_show_num_2_2(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的区号 区号最大值加一：807  807 41 200/210  807 41 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('807', *self.map_area_loc)
        self.send_keys('41', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('807', *self.PDT_area_loc)
        self.send_keys('41', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        # element = self.find_element(*(By.LINK_TEXT, '800-41-200'))
        # self.del_()
        if element:
            return False
        return True


    def user_map_show_num_2_3(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的区号 区号为英文字母：aaa  aaa 41 200/210  aaa 41 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('aaa', *self.map_area_loc)
        self.send_keys('41', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('aaa', *self.PDT_area_loc)
        self.send_keys('41', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        # element = self.find_element(*(By.LINK_TEXT, '800-41-200'))
        # self.del_()
        if element:
            return False
        return True

    def user_map_show_num_2_4(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的区号 区号为中文：警察  警察 41 200/210  警察 41 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('警察', *self.map_area_loc)
        self.send_keys('41', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('警察', *self.PDT_area_loc)
        self.send_keys('41', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        # element = self.find_element(*(By.LINK_TEXT, '800-41-200'))
        # self.del_()
        if element:
            return False
        return True

    def user_map_show_num_2_5(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的区号 区号为两位数字：33 33 41 200/210  33 41 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('33', *self.map_area_loc)
        self.send_keys('41', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('33', *self.PDT_area_loc)
        self.send_keys('41', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        # element = self.find_element(*(By.LINK_TEXT, '800-41-200'))
        # self.del_()
        if element:
            return False
        return True

    def user_map_show_num_2_6(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的队号 队号为最小值减一：19  328 19 200/210  328 19 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('19', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('19', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_7(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的队号 队号为最大值加一：90  328 90 200/210  328 90 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('90', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('90', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True


    def user_map_show_num_2_8(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的队号 队号为英文字母：aa  328 aa 200/210  328 aa 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('aa', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('aa', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_9(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的队号 队号为中文：警察  328 警察 200/210  328 警察 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('警察', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('警察', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_10(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的队号 队号为符号：%^  328 %^ 200/210  328 %^ 300/310
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('%^', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('%^', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_11(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的个号 个号为最大值加一：900  328 40 900/355  328 40 355/900
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('40', *self.map_team_loc)
        self.send_keys('900', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('40', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('900', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_12(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的个号 个号为最小值减一：199  328 40 199/355  328 40 355/199
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('40', *self.map_team_loc)
        self.send_keys('199', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('40', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('199', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_13(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的个号 个号为英文字母：aaa  328 40 aaa/355  328 40 355/aaa
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('40', *self.map_team_loc)
        self.send_keys('aaa', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('40', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('aaa', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_14(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的个号 个号为中文：成都市  328 40 成都市/355  328 40 355/成都市
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('40', *self.map_team_loc)
        self.send_keys('成都市', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('40', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('成都市', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_2_15(self):
        #进入用户映射页面 验证 配置一条新的用户号码映射范围 错误的个号 个号为符号：%^&  328 40 %^&/355  328 40 355/%^&
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('328', *self.map_area_loc)
        self.send_keys('40', *self.map_team_loc)
        self.send_keys('%^&', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('328', *self.PDT_area_loc)
        self.send_keys('40', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('%^&', *self.PDT_individual_loc_2)
        element = self.find_element(*self.map_add_btn_loc)
        if element:
            return False
        return True

    def user_map_show_num_3(self):
        #进入用户映射页面 验证 配置用户号码映射范围 添加一条已存在的范围
        self.come_iframe_page()
        self.find_element(*self.user_map_loc).click()
        self.send_keys('445', *self.map_area_loc)
        self.send_keys('30', *self.map_team_loc)
        self.send_keys('200', *self.map_individual_loc_1)
        self.send_keys('210', *self.map_individual_loc_2)
        self.send_keys('445', *self.PDT_area_loc)
        self.send_keys('30', *self.PDT_team_loc)
        self.send_keys('300', *self.PDT_individual_loc_1)
        self.send_keys('310', *self.PDT_individual_loc_2)
        self.find_element(*self.map_add_btn_loc).click()
        element = self.find_element(*self.map_alert_loc)
        self.find_element(*(By.XPATH, '/html/body/div[2]/div[2]/button[2]')).click()
        if element:
            return True
        return False

    def local_online_user(self):
        #进入本地在线用户 检查显示数量
        num = self.find_element(*(By.ID, 'radioNumber')).text
        self.come_iframe_page()
        self.find_element(*self.local_online_user_loc).click()
        elements = self.find_elements(*self.LOU_show_num)
        if str(len(elements))==num:
            return "pass"
        return "fail"

    def local_online_user_page(self):
        #进入本地在线用户 检查分页
        self.come_iframe_page()
        self.find_element(*self.local_online_user_loc).click()
        self.send_keys('1',*self.LOU_input_loc)
        self.send_enter(*self.LOU_input_loc)
        sleep(1)
        elements = self.find_elements(*self.LOU_show_num)
        print(len(elements))
        return str(len(elements))



