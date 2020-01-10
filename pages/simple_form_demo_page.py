from base_page import BasePage
from selenium.webdriver.common.by import By


class SimpleFormDemoPage(BasePage):

    text_input_field = (By.XPATH, "//input[@id='user-message']")
    show_message_btn = (By.XPATH, "//button[text()='Show Message']")
    message_field = (By.XPATH, "//span[@id='display']")

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


