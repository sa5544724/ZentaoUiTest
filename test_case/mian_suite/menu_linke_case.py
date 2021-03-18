import unittest
import HTMLTestRunner
import time
from common import set_driver
from common import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginFailCase(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.setdriver()

    def tearDown(self) -> None:  # 方法预期的返回值为None 非强制
        time.sleep(3)
        self.driver.quit()

    def test_my_link(self):
        login.login(self.driver, 'test01', 'newdream123')
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

    def test_product_link(self):
        login.login(self.driver, 'test01', 'newdream123')
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
        self.assertTrue(EC.title_is("產品主頁 - 禪道"))



if __name__  ==  '__main__':
   unittest.main()
