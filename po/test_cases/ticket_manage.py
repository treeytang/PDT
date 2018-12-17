import re
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_obj.base import Page
from time import sleep




class Ticket_Manage_Query(Page):
    '''
        话单管理--话单查询页面
        默认进入到话单查询页面
    '''


    #进入话单管理页面--默认进入话单查询  定位
    ticket_come_loc = (By.XPATH, '//*[@id="menu600"]/div[1]/a')
    #切换到嵌套表单定位
    ticket_iframe_id = 'mainFrame'
    #验证进入表单定位
    iframe_verify = (By.CLASS_NAME, 'panel-heading')
    #系统提示弹窗定位
    hint_cancel = (By.CLASS_NAME, 'jbox-close')


    # 查询  起始时间查询定位
    start_time_loc = (By.ID, 'startTime-th')
    # 查询 1 天定位
    one_day_loc = (By.XPATH, '//*[@id="oneday"]/a')
    # 查询 7 天定位
    one_week_loc = (By.XPATH, '//*[@id="oneweek"]/a')
    # 查询 30 天定位
    one_month_loc = (By.XPATH, '//*[@id="onemonth"]/a')
    # 查询 自定义 天定位
    custom_loc = (By.XPATH, '//*[@id="custom"]/a')


    #自定义查询起始输入框定位
    start_date_loc = (By.NAME, "beginDate")
    #自定义查询结束输入框定位
    end_date_loc = (By.ID, "endDate")




    #定义一页显示多少条定位
    page_any_loc = (By.ID,"page_any")
    #以一条为基准，获取条数定位
    page_num_loc = (By.XPATH, '//*[@id="pagination"]/ul/li[11]/a')



    # 话单查询 列表显示数量与实际数量 行定位
    table_line = (By.CLASS_NAME, 'contentbody')
    # 翻页定位
    next_page = (By.LINK_TEXT, '下一页 »')
    #查询到的数量定位
    query_num_loc = (By.XPATH, '//*[@id="pagination"]/ul')#//*[@id="pagination"]/ul



    # 主叫用户按钮定位
    calling_user_loc = (By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[2]')
    # 主叫用户输入框定位
    calling_user_box_loc = (By.ID, "callingNo")


    # 被叫用户按钮定位
    called_user_loc = (By.XPATH, '//*[@id="contentTable"]/tbody[1]/tr/th[3]')
    # 被叫用户输入框定位
    called_user_box_loc = (By.ID, "calledNo")


    # 会话类型定位
    session_type_loc = (By.ID, "sessionType-th")
    # 注册/注销定位
    reg_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[1]/span')
    # 短信/彩信定位
    SMS_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[3]/span')
    # GPS定位
    GPS_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[4]/span')
    # 摇晕/复活定位
    stun_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[5]/span')
    # 重组/去重组定位
    group_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[6]/span')
    # 手机编程定位
    mobi_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[7]/span')
    # 越区转换
    over_loc = (By.XPATH, '//*[@id="sessionType-th"]/div[3]/div[8]/span')





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
        sleep(3)




    #查询数量
    def query_num(self):
        sleep(1)
        js = "var q=document.documentElement.scrollTop=1000000"
        self.script(js)
        return self.find_element(*self.query_num_loc)
    # 获取分页中显示的数量
    def get_query_num(self):
        a = self.query_num().text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d', a))
        # print("查询条数共计：%s条" % s)
        return s

    # 进入表单页面
    def come_ticket(self):
        self.find_element(*self.ticket_come_loc).click()
        # 进入到右侧表单
        self.switch_frame(self.ticket_iframe_id)

        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        # 出现弹窗，返回上一层表单
        self.switch_to_default()
        if self.find_element(*self.hint_cancel):
            # 关闭提示窗口
            self.find_element(*self.hint_cancel).click()
            self.switch_frame(self.ticket_iframe_id)
            js = "var q=document.documentElement.scrollTop=10000"
            self.script(js)

    #指定时间查询主叫用户对应的类型
    def designate_time(self, calling_user):
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.start_date_loc).send_keys("2018-11-01 00:00:00")
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.end_date_loc).send_keys("2018-11-30 23:59:59")
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.end_date_loc).click()
        self.find_element(*self.end_date_loc).send_keys(Keys.ENTER)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        self.find_element(*self.page_any_loc).send_keys("1")
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        ActionChains(self.driver).move_to_element(self.find_element(*self.calling_user_loc)).perform()
        self.find_element(*self.calling_user_loc).click()
        self.find_element(*self.calling_user_box_loc).send_keys(calling_user)
        self.find_element(*self.calling_user_box_loc).send_keys(Keys.ENTER)
        sleep(1)
        ActionChains(self.driver).move_to_element(self.find_element(*self.session_type_loc)).perform()


    #指定时间查询被叫用户对应的类型
    def designate_time_called(self, called_user, start_time="2018-11-01 00:00:00", end_time="2018-11-30 23:59:59"):
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.start_date_loc).send_keys(start_time)
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.end_date_loc).send_keys(end_time)
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.end_date_loc).click()
        self.find_element(*self.end_date_loc).send_keys(Keys.ENTER)
        js = "var q=document.documentElement.scrollTop=10000"
        self.script(js)
        # 每页显示多少条
        self.find_element(*self.page_any_loc).send_keys("1")
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        # 输入查询用户
        ActionChains(self.driver).move_to_element(self.find_element(*self.called_user_loc)).perform()
        sleep(1)
        self.find_element(*self.called_user_loc).click()
        self.find_element(*self.called_user_box_loc).send_keys(called_user)
        self.find_element(*self.called_user_box_loc).send_keys(Keys.ENTER)
        sleep(1)
        ActionChains(self.driver).move_to_element(self.find_element(*self.session_type_loc)).perform()












    # 验证进入话单管理_话单查询页面
    def come_query_verify(self):
        self.find_element(*self.ticket_come_loc).click()
        # 进入到右侧表单
        self.switch_frame(self.ticket_iframe_id)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.script(js)
        # # 出现弹窗，返回上一层表单
        # self.switch_to_default()
        # if self.find_element(*self.hint_cancel):
        #     # 关闭提示窗口
        #     self.find_element(*self.hint_cancel).click()
        #     self.switch_frame(self.ticket_iframe_id)
        #     js = "var q=document.documentElement.scrollTop=10000"
        #     self.script(js)
        # sleep(2)
        # self.find_element(*self.next_page).click()
        return self.find_element(*self.iframe_verify).text



    #验证话单查询显示数量与实际数量   7  天
    def query_num_verify(self):
        self.come_ticket()
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.one_week_loc).click()
        a = self.query_num().text
        s = a.split("\n")
        a = s.pop()
        s = ""
        s = s.join(re.findall('\d',a))
        print("查询条数共计：%s条"%s)
        self.find_element(*self.page_any_loc).send_keys("1")
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        query_num = self.find_element(*self.page_num_loc).text
        if str(s)==query_num:
            return 'ok'
        else:
            return 'fail'

    def page_define_num(self):
        self.come_ticket()
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.one_week_loc).click()
        input_num = str(random.randrange(1,10))
        print(input_num)
        self.find_element(*self.page_any_loc).send_keys(input_num)
        self.find_element(*self.page_any_loc).send_keys(Keys.ENTER)
        num = self.find_elements(*self.table_line)
        check_num = 0
        for i in num:
            check_num += 1
        print(check_num)
        if input_num==check_num:
            return "ok"
        else:
            return "fail"



    def custom_time_query1(self):
        '''自定义时间查询 正确的起止时间'''
        self.come_ticket()
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.start_date_loc).send_keys("2018-11-12 00:00:00")
        self.find_element(*self.end_date_loc).send_keys("2018-12-12 00:00:00")
        sleep(3)
        self.find_element(*self.end_date_loc).send_keys(Keys.ENTER)
        # sleep(3)
        if self.find_element(*self.table_line):
            sleep(3)
            return "ok"
        else:
            sleep(3)
            return "fail"

    def custom_time_query2(self):
        '''自定义时间查询 正确的起始时间，超期的结束时间'''
        self.come_ticket()
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.start_date_loc).send_keys("2018-01-01 00:00:00")
        self.find_element(*self.end_date_loc).send_keys("2019-12-12 23:59:59")
        self.find_element(*self.end_date_loc).send_keys(Keys.ENTER)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self.alert_location()))
            print("找到了alert")
            return "出现弹窗"
        except:
            print("没有找到alert")

            return "没有弹窗"


    def custom_time_query3(self):
        '''自定义时间查询 正确的起始时间，延后的结束时间'''
        self.come_ticket()
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.start_date_loc).send_keys("2018-12-12 00:00:00")
        self.find_element(*self.end_date_loc).send_keys("2018-10-10 23:59:59")
        self.find_element(*self.end_date_loc).send_keys(Keys.ENTER)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self.alert_location()))
            print("找到了alert")
            return "出现弹窗"
        except:
            print("没有找到alert")

            return "没有弹窗"

    def custom_time_query4(self):
        '''自定义时间查询 超期的起始时间，正确的结束时间'''
        self.come_ticket()
        ActionChains(self.driver).move_to_element(self.find_element(*self.start_time_loc)).perform()
        self.find_element(*self.custom_loc).click()
        self.find_element(*self.start_date_loc).send_keys("2019-12-12 00:00:00")
        self.find_element(*self.end_date_loc).send_keys("2018-12-12 23:59:59")
        self.find_element(*self.end_date_loc).send_keys(Keys.ENTER)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self.alert_location()))
            print("找到了alert")
            return "出现弹窗"
        except:
            print("没有找到alert")
            return "没有弹窗"


    def query_calling_voc_num(self):
        '''查询用户2018/11/1到2018/11/30主叫语音数量'''
        self.come_ticket()
        calling_user = "445101"
        self.designate_time(calling_user)
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s


    def query_calling_reg_num(self):
        '''查询用户2018/11/1到2018/11/30主叫注册数量'''
        self.come_ticket()
        calling_user = "445101"
        self.designate_time(calling_user)
        self.find_element(*self.reg_loc).click()
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s

    def query_calling_sms_num(self):
        '''查询用户2018/11/1到2018/11/30主叫短信数量'''
        self.come_ticket()
        calling_user = "445101"
        self.designate_time(calling_user)
        self.find_element(*self.SMS_loc).click()
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s


    def query_calling_gps_num(self):
        '''查询用户2018/11/1到2018/11/30主叫gps数量'''
        self.come_ticket()
        calling_user = '445105'
        self.designate_time(calling_user)
        self.find_element(*self.GPS_loc).click()
        # 获取查询条数
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s


    def query_called_voc_num(self):
        '''查询用户2018/11/1到2018/11/30被叫数量'''
        self.come_ticket()
        called_user = "44530212"
        self.designate_time_called(called_user)
        # 获取查询条数
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s


    def query_called_reg_num(self):
        '''查询用户2018/11/1到2018/11/30被叫 注册 数量'''
        self.come_ticket()
        called_user = "4459601"
        self.designate_time_called(called_user)
        self.find_element(*self.reg_loc).click()
        # 获取查询条数
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s

    def query_called_sms_num(self):
        '''查询用户2018/11/1到2018/11/30被叫 注册 数量'''
        self.come_ticket()
        called_user = "44530211"
        self.designate_time_called(called_user)
        self.find_element(*self.SMS_loc).click()
        # 获取查询条数
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s

    def query_called_gps_num(self):
        '''查询用户2018/11/1到2018/11/30被叫 gps 数量'''
        self.come_ticket()
        called_user = "44530211"
        self.designate_time_called(called_user)
        self.find_element(*self.GPS_loc).click()
        # 获取查询条数
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s


    def query_called_stun_num(self):
        '''查询用户2018/11/1到2018/11/30被叫 gps 数量'''
        self.come_ticket()
        called_user = "62224501"
        start_time = "2018-09-01 00:00:00"
        end_time = "2018-09-30 23:59:59"
        self.designate_time_called(called_user, start_time, end_time)
        self.find_element(*self.stun_loc).click()
        # 获取查询条数
        s = self.get_query_num()
        print("查询条数共计：%s条" % s)
        return s