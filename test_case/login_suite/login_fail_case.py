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

    def test_login_01(self):
        login.login(self.driver, 'test01', 'newdream13')
        # actual_result=self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        # self.assertEqual(actual_result,'测试人员1','test01登录执行失败')
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))



if __name__  ==  '__main__':
   pass
