import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
            self.driver = webdriver.Chrome("/home/rmilan/codecool/test_automation/chromedriver.exe")
            self.driver.maximize_window()

    def tearDown(self):
            self.driver.quit()

