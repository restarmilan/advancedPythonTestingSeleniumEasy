from selenium.webdriver.common.by import By

from base_page import BasePage


class CheckboxDemoPage(BasePage):
    checkbox_options = (By.XPATH, "//input[@class='cb1-element']")
    checkbox_button = (By.XPATH, "//input[@id='check1']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_checkbox_demo_page(self):
        super().navigate_to("basic-checkbox-demo.html")

    def get_checkbox_button_value(self):
        return self.driver.find_element(*self.checkbox_button).get_attribute('value')

    def click_on_multiple_checkbox(self, inputs, value=1):
        for i in range(len(inputs)):
            if inputs[i] == value:
                self.driver.find_elements(*self.checkbox_options)[i].click()
