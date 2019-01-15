from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from comm.read_config import GetConfig
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Page(object):

    '''
    页面基础类，用于所有页面的继承
    '''

    base_url = 'http://192.168.1.192:8080/nmp'
    def __init__(self, selenium_driver, base_url=base_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def on_page(self):
        #return (self.driver.current_url).encode('utf-8') == (self.base_url + self.url)
        print(self.driver.current_url)
        return self.driver.current_url == (self.base_url + self.url)


    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
        # 确保所有元素是可见的
        # 注意：以下入参为元组的元素，需要加*。python存在这种特性，就是将入参放在元组里。
        #WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
        # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未能找到 %s 元素"%(self, loc))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def script(self, src):
        return self.driver.execute_script(src)

    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    def switch_to_default(self):
        return self.driver.switch_to_default_content()

    def alert_location(self):
        return self.driver.switch_to_alert()

    def send_enter(self,*loc):
        return self.find_element(*loc).send_keys(Keys.ENTER)

    def url(self):
        return self.driver.current_url

    def select(self, *loc):
        return Select(self.driver.find_element(*loc))


    def send_keys(self, value, *loc, clear_first=True, click_first=True):
        try:
            # getattr相当于self.loc
            # loc = getattr(self, "%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))