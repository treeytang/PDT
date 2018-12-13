import unittest
from .driver import browser


#初始化单元测试框架，以Chrome浏览器为驱动

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

