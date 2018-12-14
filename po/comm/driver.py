from selenium import webdriver

# 启动浏览器
def browser():
        driver = webdriver.Chrome()
        return driver
