import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
            self.driver = webdriver.Chrome("/home/rmilan/codecool/test_automation/chromedriver.exe")
            self.driver.maximize_window()

    def tearDown(self):
            self.driver.quit()

    @staticmethod
    def run_single(test_case, test_to_run):
        test_case.setUp()
        test_to_run()
        test_case.tearDown()
