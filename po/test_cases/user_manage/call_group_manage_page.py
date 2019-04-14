from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep



class Call_Group(Page):
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
    call_group_manage_loc = (By.LINK_TEXT, '通话组管理')
    #嵌套页面定位
    iframe_loc = 'mainFrame'


    #每页显示输入框定位
    page_show_num_input = (By.XPATH, '//*[@id="freestyle"]/div[1]/div[1]/div/div[2]/div[1]/div[5]/input')
    #通话组列表页面 显示数量elements定位
    call_group_list_show_num = (By.XPATH, '//*[@id="muserList"]/tr')
    #组用户号码
    group_user_num_loc = (By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/th[2]')
    #开始号码输入框定位
    start_num_loc = (By.ID, 'number_start')
    #结束号码输入框定位
    end_num_loc = (By.ID, 'number_end')
    #列表页删除按钮定位
    del_btn_loc = (By.XPATH, '//*[@id="muserList"]/tr/td[10]/button')
    #复选框全选定位
    checkbox_all_loc = (By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/th[1]/input')
    #下方删除按钮定位
    del_loc = (By.ID, 'delete')




    #添加按钮定位
    add_group_loc = (By.ID, 'add')
    #区号定位
    group_area_code_loc = (By.XPATH, '//*[@id="ssi"]/div[3]/span[1]/input')
    #队号定位
    group_team_code_loc = (By.XPATH, '//*[@id="ssi"]/div[3]/span[4]/input')
    group_team_code_loc_1 = (By.XPATH, '//*[@id="ssi"]/div[3]/span[10]/input')
    #组号定位
    group_group_code_loc = (By.XPATH, '//*[@id="ssi"]/div[3]/span[6]/input')
    group_group_code_loc_1 = (By.XPATH, '//*[@id="ssi"]/div[3]/span[12]/input')
    #确定按钮定位
    ensure_loc = (By.ID, 'add')
    #系统提示弹窗确定定位
    alert_sure_loc = (By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[1]')
    #系统提示弹窗取消定位
    alert_cancel_loc = (By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button[2]')
    #替换提示窗定位
    replace_loc = (By.XPATH, '/html/body/div[3]')
    #替换提示窗口 是 定位
    replace_yes_loc = (By.XPATH, '/html/body/div[3]/div[3]/div[1]/button[1]')
    #替换提示窗口 否 定位
    replace_no_loc = (By.XPATH, '/html/body/div[3]/div[3]/div[1]/button[2]')
    #替换提示窗口 取消 定位
    replace_cancel_loc = (By.XPATH, '/html/body/div[3]/div[3]/div[1]/button[3]')
    #替换提示窗口 选择框 定位
    replace_choice_loc = (By.XPATH, '/html/body/div[3]/div[3]/div[2]/input')
    #用户名称定位
    user_name_loc = (By.ID, 'single-air_alias')





    #漫游组列表定位
    roma_gsi_loc = (By.LINK_TEXT, '漫游组列表')
    #每页显示数量输入框定位
    gsi_show_num_input = (By.XPATH, '//*[@id="freestyle"]/div/div/div[1]/div[2]/div[1]/div[5]/input')
    #添加按钮定位
    gis_add_loc = (By.ID, 'add')
    # 区号定位
    gis_area_code_loc = (By.XPATH, '//*[@id="ssi"]/div[2]/span[1]/input')
    # 队号定位
    gis_team_code_loc = (By.XPATH, '//*[@id="ssi"]/div[2]/span[4]/input')
    gis_team_code_loc_1 = (By.XPATH, '//*[@id="ssi"]/div[2]/span[10]/input')
    # 组号定位
    gis_group_code_loc = (By.XPATH, '//*[@id="ssi"]/div[2]/span[6]/input')
    gis_group_code_loc_1 = (By.XPATH, '//*[@id="ssi"]/div[2]/span[12]/input')
    #添加页面确定按钮定位
    gis_ensure_loc = (By.ID, 'add')
    #组用户号码定位
    gis_user_code_loc = (By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/td[2]')
    #复选框定位
    gis_checkbox_loc = (By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/td[1]/input')
    #用户名称输入框定位
    gis_user_name_loc = (By.ID, 'single-air_alias')
    # 通话配置定位
    call_config_loc = (By.XPATH, '//*[@id="freestyle"]/div[1]/div[2]/div/div[2]/div[1]')
    #优先等级定位
    gis_priority_loc = (By.XPATH, '//*[@id="priority"]/div/select')
    #通话限时定位
    gis_call_time_loc = (By.ID, 'session_timer')
    #组呼呼出策略定位
    gis_group_call_loc = (By.XPATH, '//*[@id="out_policy"]/select')
    #主叫限定再指定基站定位
    gis_calling_BS_loc = (By.XPATH, '//*[@id="out_sub_policy_0"]/select')
    #静态组分配呼出范围策略
    gis_static_range_loc = (By.XPATH, '//*[@id="out_sub_policy_1"]/select')









    def come_iframe_page(self):
        #进入嵌套页面公用函数 默认进入通话组列表
        self.find_element(*self.user_manage_loc).click()
        self.find_element(*self.call_group_manage_loc).click()
        self.switch_frame(self.iframe_loc)



    def verify_show_num(self):
        #验证页面显示数量
        self.come_iframe_page()
        sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        self.send_keys('800', *self.page_show_num_input)
        self.send_enter(*self.page_show_num_input)
        sleep(1)
        elements = self.find_elements(*self.call_group_list_show_num)
        return str(len(elements))


    def verify_show_num_1(self):
        #验证页面显示数量 通过每页显示数量定量显示
        self.come_iframe_page()
        sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        self.send_keys('1', *self.page_show_num_input)
        self.send_enter(*self.page_show_num_input)
        sleep(1)
        elements = self.find_elements(*self.call_group_list_show_num)
        return str(len(elements))


    '''
        区号：328-806  队号：20-89  组号：900-999
    '''
    def system_hint(self, *loc):
        #系统提示窗处理
        self.switch_to_default()
        self.find_element(*loc).click()
        self.switch_frame(self.iframe_loc)


    def add_group_1(self):
        #添加组 只输入号码范围80040900/910
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('800', *self.group_area_code_loc)
        self.send_keys('40', *self.group_team_code_loc)
        self.send_keys('900', *self.group_group_code_loc)
        self.send_keys('40', *self.group_team_code_loc_1)
        self.send_keys('910', *self.group_group_code_loc_1)
        #测试取消按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_cancel_loc)
        #测试确定按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)

        #查看是否添加成功
        self.find_element(*self.group_user_num_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_keys('80040910', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(3)
        elements = self.find_elements(*self.call_group_list_show_num)
        sleep(2)
        #循环删除所添加的组号码
        while True:
            element = self.find_element(*self.del_btn_loc)
            if element:
                self.find_element(*self.del_btn_loc).click()
                self.system_hint(*self.alert_sure_loc)
                sleep(2)
            else:
                break
        if len(elements)==11:
            return 'pass'
        return 'fail'

    def add_group_1_1(self):
        #添加组 只输入号码范围80040900/910
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('800', *self.group_area_code_loc)
        self.send_keys('40', *self.group_team_code_loc)
        self.send_keys('900', *self.group_group_code_loc)
        self.send_keys('40', *self.group_team_code_loc_1)
        self.send_keys('910', *self.group_group_code_loc_1)
        #测试取消按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_cancel_loc)
        #测试确定按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        #查看是否添加成功
        self.find_element(*self.group_user_num_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_keys('80040910', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(3)
        elements = self.find_elements(*self.call_group_list_show_num)
        sleep(2)
        #复选框全选删除所添加的组号码
        self.find_element(*self.checkbox_all_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        # sleep(5)
        return str(len(elements))


    def add_group_1_2(self):
        #添加号码 只输入号码范围80040900 命名用户名称为：成都测试
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('800', *self.group_area_code_loc)
        self.send_keys('40', *self.group_team_code_loc)
        self.send_keys('900', *self.group_group_code_loc)
        self.send_keys('成都测试', *self.user_name_loc)
        #测试取消按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_cancel_loc)
        #测试确定按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        #查看是否添加成功
        self.find_element(*self.group_user_num_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(3)
        elements = self.find_elements(*self.call_group_list_show_num)
        sleep(1)
        #复选框全选删除所添加的组号码
        self.find_element(*self.checkbox_all_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        # sleep(5)
        return str(len(elements))

    def add_group_1_3(self):
        #添加号码 只输入号码范围80040900 不填写用户名称
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('800', *self.group_area_code_loc)
        self.send_keys('40', *self.group_team_code_loc)
        self.send_keys('900', *self.group_group_code_loc)
        #测试确定按钮
        self.find_element(*self.ensure_loc).click()
        #查看是否出现系统提示弹窗来确认添加
        self.switch_to_default()
        if self.find_element(*self.alert_sure_loc):
            return False
        return True

    def add_group_1_4(self):
        #添加号码 只输入号码范围80040900 用户名称大于7个字符 验证：系统是否自动删除了第七位后的字符
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('800', *self.group_area_code_loc)
        self.send_keys('40', *self.group_team_code_loc)
        self.send_keys('900', *self.group_group_code_loc)
        self.send_keys('一二三四五六七八九', *self.user_name_loc)
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        # 查看是否添加成功
        self.find_element(*(By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/th[5]')).click()
        self.send_keys('一二三四五六七', *(By.ID, 'alias'))
        self.send_enter(*(By.ID, 'alias'))
        sleep(3)
        elements = self.find_elements(*self.call_group_list_show_num)
        sleep(2)
        # 复选框全选删除所添加的组号码
        self.find_element(*self.checkbox_all_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        # sleep(5)
        return str(len(elements))

    def add_group_1_5(self):
        #添加组 只输入号码范围80040900/910+通话配置：默认全为第一项 全选取第二项
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('800', *self.group_area_code_loc)
        self.send_keys('40', *self.group_team_code_loc)
        self.send_keys('900', *self.group_group_code_loc)
        self.send_keys('40', *self.group_team_code_loc_1)
        self.send_keys('910', *self.group_group_code_loc_1)
        self.select(*self.gis_priority_loc).select_by_value('1')
        self.send_keys('300', *self.gis_call_time_loc)
        sleep(3)
        self.find_element(*self.call_config_loc).click()
        self.select(*self.gis_group_call_loc).select_by_value('4')
        self.select(*self.gis_calling_BS_loc).select_by_value('1')
        self.select(*self.gis_static_range_loc).select_by_value('01')
        sleep(3)
        #测试确定按钮
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        #查看是否添加成功
        self.find_element(*self.group_user_num_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_keys('80040910', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(3)
        elements = self.find_elements(*self.call_group_list_show_num)
        sleep(1)
        #复选框全选删除所添加的组号码
        self.find_element(*self.checkbox_all_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        # sleep(5)
        return str(len(elements))



    def add_group_2(self):
        #添加组 添加一个以存在的组 号码范围 328 20 990/999 验证是否出现弹窗
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('328', *self.group_area_code_loc)
        self.send_keys('20', *self.group_team_code_loc)
        self.send_keys('990', *self.group_group_code_loc)
        self.send_keys('20', *self.group_team_code_loc_1)
        self.send_keys('999', *self.group_group_code_loc_1)
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        if self.find_element(*self.replace_loc):
            return True
        return False




    def add_group_3(self):
        # 添加组 添加一个以存在的组 号码范围 328 20 990/999 出现弹窗 点击取消
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('328', *self.group_area_code_loc)
        self.send_keys('20', *self.group_team_code_loc)
        self.send_keys('990', *self.group_group_code_loc)
        self.send_keys('20', *self.group_team_code_loc_1)
        self.send_keys('999', *self.group_group_code_loc_1)
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.replace_cancel_loc).click()
        if self.find_element(*self.group_area_code_loc):
            return True
        return False

    def add_group_4(self):
        # 添加组 添加一个以存在的组 号码范围 328 20 990/999 出现弹窗 点击选择框和是
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('328', *self.group_area_code_loc)
        self.send_keys('20', *self.group_team_code_loc)
        self.send_keys('990', *self.group_group_code_loc)
        self.send_keys('20', *self.group_team_code_loc_1)
        self.send_keys('999', *self.group_group_code_loc_1)
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.replace_choice_loc).click()
        self.find_element(*self.replace_yes_loc).click()
        if self.find_element(*(By.LINK_TEXT, '通话组列表')):
            return True
        return False

    def add_group_5(self):
        # 添加组 添加一个以存在的组 号码范围 328 20 990/999 出现弹窗 点击选择框和否
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('328', *self.group_area_code_loc)
        self.send_keys('20', *self.group_team_code_loc)
        self.send_keys('990', *self.group_group_code_loc)
        self.send_keys('20', *self.group_team_code_loc_1)
        self.send_keys('999', *self.group_group_code_loc_1)
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.replace_choice_loc).click()
        self.find_element(*self.replace_no_loc).click()
        if self.find_element(*(By.LINK_TEXT, '通话组列表')):
            return True
        return False

    def add_group_6(self):
        # 添加组 添加一个以存在的用户 号码范围 328 20 992 出现弹窗 点击是
        self.come_iframe_page()
        self.find_element(*self.add_group_loc).click()
        self.send_keys('328', *self.group_area_code_loc)
        self.send_keys('20', *self.group_team_code_loc)
        self.send_keys('990', *self.group_group_code_loc)
        self.send_keys('aaa', *self.user_name_loc)
        self.find_element(*self.ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.replace_yes_loc).click()
        self.find_element(*(By.XPATH, '//*[@id="muserTable"]/tbody[1]/tr/th[5]')).click()
        self.send_keys('aaa', *(By.ID, 'alias'))
        self.send_enter(*(By.ID, 'alias'))
        sleep(2)
        elements = self.find_elements(*self.call_group_list_show_num)
        print(len(elements))
        if len(elements) == 1:
            return True
        return False


    def roma_group_list(self):
        #漫游组列表
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        sleep(1)
        self.send_keys('200', *self.gsi_show_num_input)
        self.send_enter(*self.gsi_show_num_input)
        sleep(1)
        elements = self.find_elements(*self.call_group_list_show_num)
        return str(len(elements))

    def roma_group_list_1(self):
        #漫游组列表
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        sleep(1)
        self.send_keys('1', *self.gsi_show_num_input)
        self.send_enter(*self.gsi_show_num_input)
        sleep(1)
        elements = self.find_elements(*self.call_group_list_show_num)
        return str(len(elements))


    def roma_group_list_2(self):
        #漫游组列表 添加一个组800-40-990/40-999
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        # sleep(1)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.script(js)
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('800', *self.gis_area_code_loc)
        self.send_keys('40', *self.gis_team_code_loc)
        self.send_keys('990', *self.gis_group_code_loc)
        self.send_keys('40', *self.gis_team_code_loc_1)
        self.send_keys('999', *self.gis_group_code_loc_1)
        self.find_element(*self.gis_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.gis_user_code_loc).click()
        self.send_keys('80040990', *self.start_num_loc)
        self.send_keys('80040999', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(2)
        element = self.find_elements(*self.call_group_list_show_num)
        print(len(element))
        self.find_element(*self.gis_checkbox_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)

        return str(len(element))


    def roma_group_list_3(self):
        #漫游组列表 添加一个已存在的组 328-20-931/20-935
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('328', *self.gis_area_code_loc)
        self.send_keys('20', *self.gis_team_code_loc)
        self.send_keys('931', *self.gis_group_code_loc)
        self.send_keys('20', *self.gis_team_code_loc_1)
        self.send_keys('935', *self.gis_group_code_loc_1)
        self.find_element(*self.gis_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.replace_choice_loc).click()
        self.find_element(*self.replace_yes_loc).click()
        self.find_element(*self.gis_user_code_loc).click()
        if self.find_element(*self.roma_gsi_loc):
            return True
        return False

    def roma_group_list_4(self):
        #漫游组列表 添加一个已存在的组 328-20-931  用户名称为：bbb
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('328', *self.gis_area_code_loc)
        self.send_keys('20', *self.gis_team_code_loc)
        self.send_keys('931', *self.gis_group_code_loc)
        self.send_keys('bbb', *self.gis_user_name_loc)
        self.find_element(*self.gis_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.replace_choice_loc).click()
        self.find_element(*self.replace_yes_loc).click()
        self.find_element(*self.gis_user_code_loc).click()
        if self.find_element(*self.roma_gsi_loc):
            return True
        return False

    def roma_group_list_5(self):
        #漫游组列表 添加一个已存在的用户 328-20-931 不填写用户名称
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('328', *self.gis_area_code_loc)
        self.send_keys('20', *self.gis_team_code_loc)
        self.send_keys('931', *self.gis_group_code_loc)
        self.find_element(*self.gis_ensure_loc).click()
        if self.find_element(*self.gis_user_name_loc):
            return True
        return False

    def roma_group_list_6(self):
        # 漫游组列表 添加一个组80040900/910 等级为优先 通话限时为300 通话配置选项全选（默认全为第一项）第二项
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('800', *self.gis_area_code_loc)
        self.send_keys('40', *self.gis_team_code_loc)
        self.send_keys('900', *self.gis_group_code_loc)
        self.send_keys('40', *self.gis_team_code_loc_1)
        self.send_keys('910', *self.gis_group_code_loc_1)
        self.select(*self.gis_priority_loc).select_by_value('1')
        self.send_keys('300', *self.gis_call_time_loc)
        self.find_element(*self.call_config_loc).click()
        sleep(2)
        self.select(*self.gis_group_call_loc).select_by_value('4')
        self.select(*self.gis_calling_BS_loc).select_by_value('1')
        self.select(*self.gis_static_range_loc).select_by_value('01')
        self.find_element(*self.gis_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.gis_user_code_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_keys('80040910', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(2)
        element = self.find_elements(*self.call_group_list_show_num)
        print(len(element))
        self.find_element(*self.gis_checkbox_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        if len(element) == 11:
            return True
        return False



    def roma_group_list_7(self):
        # 漫游组列表 添加一个组80040900/910  其余基本信息默认   通话配置选项全选（默认全为第一项）第二项
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('800', *self.gis_area_code_loc)
        self.send_keys('40', *self.gis_team_code_loc)
        self.send_keys('900', *self.gis_group_code_loc)
        self.send_keys('40', *self.gis_team_code_loc_1)
        self.send_keys('910', *self.gis_group_code_loc_1)
        self.find_element(*self.call_config_loc).click()
        sleep(2)
        self.select(*self.gis_group_call_loc).select_by_value('4')
        self.select(*self.gis_calling_BS_loc).select_by_value('1')
        self.select(*self.gis_static_range_loc).select_by_value('01')
        self.find_element(*self.gis_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.gis_user_code_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_keys('80040910', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(2)
        element = self.find_elements(*self.call_group_list_show_num)
        print(len(element))
        self.find_element(*self.gis_checkbox_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        if len(element) == 11:
            return True
        return False

    def roma_group_list_8(self):
        # 漫游组列表 添加一个组80040900/910 等级为优先 通话限时为300 通话配置默
        self.come_iframe_page()
        self.find_element(*self.roma_gsi_loc).click()
        self.find_element(*self.gis_add_loc).click()
        sleep(1)
        self.send_keys('800', *self.gis_area_code_loc)
        self.send_keys('40', *self.gis_team_code_loc)
        self.send_keys('900', *self.gis_group_code_loc)
        self.send_keys('40', *self.gis_team_code_loc_1)
        self.send_keys('910', *self.gis_group_code_loc_1)
        self.select(*self.gis_priority_loc).select_by_value('1')
        self.send_keys('300', *self.gis_call_time_loc)
        self.find_element(*self.gis_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*self.gis_user_code_loc).click()
        self.send_keys('80040900', *self.start_num_loc)
        self.send_keys('80040910', *self.end_num_loc)
        self.send_enter(*self.end_num_loc)
        sleep(2)
        element = self.find_elements(*self.call_group_list_show_num)
        print(len(element))
        self.find_element(*self.gis_checkbox_loc).click()
        self.find_element(*self.del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        if len(element) == 11:
            return True
        return False





    #分级组管理定位
    grade_group_loc = (By.LINK_TEXT, '分级组管理')
    #页面显示element定位
    ggp_show_num_loc = (By.XPATH, '//*[@id="grade-group-list"]/tr')
    #添加按钮
    ggp_add_loc = (By.ID, 'add')
    #操作栏删除标识定位
    ggp_del_ico = (By.XPATH, '//*[@id="grade-group-list"]/tr[1]/td[8]/button')
    #复选框选择
    ggp_checkbox_only_loc = (By.XPATH, '//*[@id="grade-group-list"]/tr[1]/td[1]/input')
    #删除按钮定位
    ggp_del_loc = (By.ID, 'delete')
    #验证修改定位
    ggp_verify_modify_loc = (By.XPATH, '//*[@id="grade-group-list"]/tr[1]/td[4]')

    #分级组组号输入框定位
    ggp_grade_group_code = (By.ID, 'gsi')
    #是否启用选择框定位
    ggp_whether_use_loc = (By.ID, 'enable')
    #用户名称输入框定位
    ggp_user_name_loc = (By.ID, 'alias')
    #确定按钮定位
    ggp_ensure_loc = (By.ID, 'add')

    def grade_group(self):
        #验证分级组管理页面列表显示数量
        self.come_iframe_page()
        self.find_element(*self.grade_group_loc).click()
        elements = self.find_elements(*self.ggp_show_num_loc)
        return str(len(elements))

    def grade_group_1(self):
        #进入分级组管理页面点击添加按钮 添加分级组组号：97001 用户名称：测试  而后删除(使用列表中的删除图标删除)
        self.come_iframe_page()
        self.find_element(*self.grade_group_loc).click()
        self.find_element(*self.ggp_add_loc).click()
        self.send_keys('97001', *self.ggp_grade_group_code)
        self.send_keys('测试', *self.ggp_user_name_loc)
        self.find_element(*self.ggp_ensure_loc).click()
        self.find_element(*self.ggp_del_ico).click()
        self.system_hint(*self.alert_sure_loc)
        sleep(2)
        elements = self.find_elements(*self.ggp_show_num_loc)
        if len(elements)==6:
            return True
        return False


    def grade_group_1_1(self):
        #进入分级组管理页面点击添加按钮 添加分级组组号：97001 用户名称：测试  而后删除(使用页面下方的删除按钮删除)
        self.come_iframe_page()
        self.find_element(*self.grade_group_loc).click()
        self.find_element(*self.ggp_add_loc).click()
        self.send_keys('97001', *self.ggp_grade_group_code)
        self.send_keys('测试', *self.ggp_user_name_loc)
        self.find_element(*self.ggp_ensure_loc).click()
        self.find_element(*self.ggp_checkbox_only_loc).click()
        self.find_element(*self.ggp_del_loc).click()
        self.system_hint(*self.alert_sure_loc)
        sleep(2)
        elements = self.find_elements(*self.ggp_show_num_loc)
        if len(elements)==6:
            return True
        return False

    def grade_group_2(self):
        #进入分级组管理页面 添加分级组组号：97001 用户名称：测试 不启用 而后修改其为启用
        self.come_iframe_page()
        self.find_element(*self.grade_group_loc).click()
        self.find_element(*self.ggp_add_loc).click()
        self.send_keys('97001', *self.ggp_grade_group_code)
        self.find_element(*self.ggp_whether_use_loc).click()
        self.send_keys('测试', *self.ggp_user_name_loc)
        self.find_element(*self.ggp_ensure_loc).click()
        self.find_element(*(By.LINK_TEXT, '97001')).click()
        self.find_element(*self.ggp_whether_use_loc).click()
        sleep(1)
        self.find_element(*self.ggp_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        self.find_element(*(By.ID, 'back')).click()
        element = self.find_element(*self.ggp_verify_modify_loc).text
        print(element)
        self.find_element(*(By.XPATH, '//*[@id="grade-group-list"]/tr[1]/td[8]/button')).click()
        self.system_hint(*self.alert_sure_loc)
        if element=="启用":
            return True
        return False

    def grade_group_3(self):
        #进入分级组管理页面  查看上次上次操作修改是否成功
        self.come_iframe_page()
        self.find_element(*self.grade_group_loc).click()
        # self.find_element(*self.ggp_add_loc).click()
        # self.send_keys('97001', *self.ggp_grade_group_code)
        # self.find_element(*self.ggp_whether_use_loc).click()
        # self.send_keys('测试', *self.ggp_user_name_loc)
        # self.find_element(*self.ggp_ensure_loc).click()
        # self.find_element(*(By.LINK_TEXT, '97001')).click()
        # self.find_element(*self.ggp_whether_use_loc).click()
        # self.find_element(*self.ggp_ensure_loc).click()
        # self.system_hint(*self.alert_sure_loc)

        element = self.find_element(*self.ggp_verify_modify_loc).text
        print(element)
        self.find_element(*self.ggp_del_ico).click()
        self.system_hint(*self.alert_sure_loc)
        sleep(2)
        if element == '启用':
            return True
        return False

    def grade_group_4(self):
        #进入分级组管理页面 点击添加 添加一个已存在的组号 出现替换提示弹窗 点击确定跳转到分级组管理列表页面
        self.come_iframe_page()
        self.find_element(*self.grade_group_loc).click()
        self.find_element(*self.ggp_add_loc).click()
        self.send_keys('97002', *self.ggp_grade_group_code)
        self.find_element(*self.ggp_ensure_loc).click()
        self.system_hint(*self.alert_sure_loc)
        if self.find_element(*self.ggp_show_num_loc):
            return True
        return False





    #临时应急组定位
    temp_group_loc = (By.LINK_TEXT, '临时应急组')
    #每页显示数量输入框定位
    temp_page_show_num = (By.XPATH, '//*[@id="freestyle"]/div/div[3]/div/div[1]/div[5]/input')
    #页面显示数量element定位
    temp_show_num_loc = (By.XPATH, '//*[@id="temp-group-list"]/tr')
    #分页图标按钮定位
    temp_page_btn_loc = (By.XPATH, '//*[@id="freestyle"]/div/div[3]/div/div[1]/ul/li/a')

    #添加按钮定位
    temp_add_loc = (By.ID, 'add')
    #号码范围区号定位
    temp_area_code_loc = (By.XPATH, '//*[@id="tempgsi"]/div/div/input[1]')
    #号码范围队号定位
    temp_team_code_loc = (By.XPATH, '//*[@id="tempgsi"]/div/div/input[2]')
    #号码范围组号定位
    temp_group_code_loc = (By.XPATH, '//*[@id="tempgsi"]/div/div/input[3]')
    # 号码范围组号定位
    temp_group_code_loc_1 = (By.XPATH, '//*[@id="tempgsi"]/div/div/input[5]')
    #名称输入框定位
    temp_nameInput_loc = (By.ID, 'alias')
    #逾期时间定位
    temp_outTime_loc = (By.ID, 'expires')




    def temp_group_list(self):
        #进入临时应急组页面 验证组用户数量
        self.come_iframe_page()
        self.find_element(*self.temp_group_loc).click()
        sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        self.send_keys('100', *self.temp_page_show_num)
        self.send_enter(*self.temp_page_show_num)
        sleep(1)
        elements = self.find_elements(*self.temp_show_num_loc)
        return str(len(elements))


    def temp_group_list_1(self):
        #进入临时应急组页面 验证分页显示按钮显示是否正确
        self.come_iframe_page()
        self.find_element(*self.temp_group_loc).click()
        sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        self.send_keys('100', *self.temp_page_show_num)
        self.send_enter(*self.temp_page_show_num)
        sleep(1)
        elements = self.find_elements(*self.temp_page_btn_loc)
        return str(len(elements))


