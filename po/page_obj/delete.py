from selenium import webdriver
import unittest


class aaa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.1.192:8080/nmp/')

    def test_aa(self):
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('admin')
        self.driver.find_element_by_id('login-btn').click()
        self.driver.find_element_by_xpath('//*[@id="menu600"]/div[1]/a').click()
        self.driver.switch_to_frame('mainFrame')
        a = self.driver.find_element_by_class_name('panel-heading').text
        print(a)
