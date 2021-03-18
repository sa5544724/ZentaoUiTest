import os
from selenium import webdriver
from common.config_util import Config


def setdriver():


    Config.get_url_path
    current = os.path.dirname(__file__)
    driver_path=os.path.join(current,'../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)  # 选择Chrome浏览器
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.get_url_path)
    return driver
