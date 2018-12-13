from selenium import webdriver
import unittest,time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By


class A123(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://192.168.1.192:8080/nmp/')

        # 登录用户名的定位
        self.login_username_loc = (By.ID, 'username')
        # 登录密码的定位
        self.login_password_loc = (By.ID, 'password')
        # 登录按钮的定位
        self.login_button_loc = (By.ID, 'login-btn')
        # 登录错误提示的定位
        self.login_error_loc = (By.ID, 'loginError')
        # 登录成功用户名信息
        self.login_user_success_loc = (By.XPATH, '//*[@id="zhongduanshu"]/div[1]')

        # 登录用户名

    def login_username(self):
        self.driver.find_element(*self.login_username_loc).send_keys("admin")
        self.driver.find_element(*self.login_password_loc).send_keys("admin")
        self.driver.find_element(*self.login_button_loc).click()

    def test1(self):
        self.login_username()
        self.driver.find_element(By.XPATH, '//*[@id="menu600"]/div[1]/a').click()
        self.driver.switch_to_frame("mainFrame")
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID, 'startTime-th')).perform()
        self.driver.find_element(By.XPATH, '//*[@id="oneweek"]/a').click()
        self.driver.implicitly_wait(10)

        js = "var q=document.documentElement.scrollTop=20000"
        self.driver.execute_script(js)
        self.driver.implicitly_wait(10)

        print(self.driver.find_element(By.XPATH, '//*[@id="pagination"]/ul').text)
        time.sleep(10)


if __name__=="__main__":
    unittest.main()


