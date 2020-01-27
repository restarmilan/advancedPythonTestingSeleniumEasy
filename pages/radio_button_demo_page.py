from selenium.webdriver.common.by import By

from base_page import BasePage


class RadioButtonDemoPage(BasePage):
    radio_buttons = (By.XPATH, "//input[@name='optradio']")
    get_checked_value = (By.XPATH, "//button[@id='buttoncheck']")
    confirmation_msg = (By.XPATH, "//p[@class='radiobutton']")
    gender_group = (By.XPATH, "//input[@name='gender']")
    age_group = (By.XPATH, "//input[@name='ageGroup']")
    get_values_multiple_rb = (By.XPATH, "//button[text()='Get values']")
    confirmation_msg_multiple_rb = (By.XPATH, "//p[@class='groupradiobutton']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_radio_buttons_demo_page(self):
        super().navigate_to("basic-radiobutton-demo.html")

    def click_to_radio_button(self, elements1, value1, elements2=None, value2=None):
        self.select_and_click_web_element(elements1, value1)
        if value2 is not None and elements2 is not None:
            self.select_and_click_web_element(elements2, value2)

    @staticmethod
    def select_and_click_web_element(elements, value):
        for i in range(len(elements)):
            if elements[i].get_attribute("value") == value:
                elements[i].click()

    def click_simple_radio_buttons(self, value):
        self.click_to_radio_button(self.driver.find_elements(*self.radio_buttons), value)

    def click_multiple_radio_buttons(self, value1, value2):
        self.click_to_radio_button(self.driver.find_elements(*self.gender_group), value1,
                                   self.driver.find_elements(*self.age_group), value2)

    def get_selected_value_single_radio_button(self):
        self.driver.find_element(*self.get_checked_value).click()

    def get_selected_values_multiple_radio_buttons(self):
        self.driver.find_element(*self.get_values_multiple_rb).click()

    def get_confirmation_message_single_radio_button(self):
        return self.driver.find_element(*self.confirmation_msg).text

    def get_confirmation_message_multiple_radio_button(self):
        return self.driver.find_element(*self.confirmation_msg_multiple_rb).text
