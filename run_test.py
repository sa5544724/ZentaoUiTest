import os
import time
import unittest
import HTMLTestRunner
now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
current = os.path.dirname(__file__)
report_path = os.path.join(current, 'report')
case_path = os.path.join(current, 'test_case')
htlm_path = os.path.join(report_path, 'report_%s.html'%now_time)

discover=unittest.defaultTestLoader.discover(start_dir=case_path,
                                             pattern='*_case.py',
                                             top_level_dir=case_path)

main_suite=unittest.TestSuite()
main_suite.addTest(discover)

file = open(htlm_path,'wb')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                            title='whytest',
                                            description='测试描述')
html_runner.run(main_suite)