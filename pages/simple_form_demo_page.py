from selenium.webdriver.common.by import By

from base_page import BasePage


class SimpleFormDemoPage(BasePage):
    text_input_field = (By.XPATH, "//input[@id='user-message']")
    show_message_btn = (By.XPATH, "//button[text()='Show Message']")
    message_field = (By.XPATH, "//span[@id='display']")
    value_a_field = (By.XPATH, "//input[@id='sum1']")
    value_b_field = (By.XPATH, "//input[@id='sum2']")
    get_total_button = (By.XPATH, "//button[text()='Get Total']")
    added_values = (By.XPATH, "//span[@id='displayvalue']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_simple_demo_form_page(self):
        super().navigate_to("basic-first-form-demo.html")

    def set_user_input_to_simple_input_field(self, message):
        self.driver.find_element(*self.text_input_field).send_keys(message)

    def click_on_confirmation_button(self):
        self.driver.find_element(*self.show_message_btn).click()

    def get_user_message(self):
        return self.driver.find_element(*self.message_field).text

    def set_double_user_input(self, value1, value2):
        self.driver.find_element(*self.value_a_field).send_keys(value1)
        self.driver.find_element(*self.value_b_field).send_keys(value2)

    def add_values(self):
        self.driver.find_element(*self.get_total_button).click()

    def get_added_values(self):
        return self.driver.find_element(*self.added_values).text
