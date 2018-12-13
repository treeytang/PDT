from selenium import webdriver
import os
from comm.time_now import time_now

# 截图函数


def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('comm')[0]
    file_name = time_now() + file_name
    file_path = base + "report/image/" + file_name
    driver.get_screenshot_as_file(file_path)

