from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://192.168.1.192:8080/nmp/")
driver.maximize_window()
driver.find_element_by_id('username').send_keys("thy")
driver.find_element_by_id('password').send_keys("admin")
driver.find_element_by_id('login-btn').click()
driver.find_element_by_id('radioNumber').click()
driver.switch_to_frame('mainFrame')
# element = driver.find_element_by_xpath('//*[@id="regUserList"]/tr[1]/td[11]/button')
for i in range(138):
    element = driver.find_element_by_xpath('//*[@id="regUserList"]/tr[1]/td[11]/button')
    element.click()
    driver.switch_to_default_content()
    driver.find_element_by_xpath('//*[@id="jbox-state-state0"]/div[2]/button[1]').click()
    driver.switch_to_frame('mainFrame')
    sleep(1)
print('over')
driver.quit()