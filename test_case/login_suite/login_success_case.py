import unittest
import HTMLTestRunner
import time
from common import set_driver
from common import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginSuccessCase(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.setdriver()

    def tearDown(self) -> None:  # 方法预期的返回值为None 非强制
        time.sleep(3)
        self.driver.quit()

    def test_login_01(self):
        login.login(self.driver, 'test01', 'newdream123')
        # actual_result=self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        # self.assertEqual(actual_result,'测试人员1','test01登录执行失败')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'), '测试人员1'),
                        'test01登录执行失败')

    def test_login_02(self):
        login.login(self.driver, 'test02', 'newdream123')
        actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(actual_result, '测试人员2', 'test登录执行失败')


if __name__ == '__main__':
    pass
    # suite01 = unittest.TestSuite(unittest.makeSuite(Logintest))
    # now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # file = open('result_%s.html' % now_time, 'wb')
    # html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
    #                                             title='whytest',
    #                                             description='测试描述')
    # html_runner.run(suite01)
