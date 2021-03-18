import os
from selenium import webdriver
from selenium.webdriver.common.by import By
def login(driver,username,password):
    driver.find_element(By.XPATH ,'//input[@class="form-control" and @name="account"]').send_keys(username)
    driver.find_element(By.XPATH ,'//input[@class="form-control" and @name="password"]').send_keys(password)
    driver.find_element(By.XPATH ,'//button[@id="submit"]').click()

