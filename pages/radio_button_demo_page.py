from selenium.webdriver.common.by import By

from base_page import BasePage


class RadioButtonDemoPage(BasePage):
    radio_buttons = (By.XPATH, "//input[@name='optradio']")
    get_checked_value = (By.XPATH, "//button[@id='buttoncheck']")
    confirmation_msg = (By.XPATH, "//p[@class='radiobutton']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_radio_buttons_demo_page(self):
        super().navigate_to("basic-radiobutton-demo.html")

    def click_to_radio_button(self, value):
        for i in range(len(self.driver.find_elements(*self.radio_buttons))):
            if self.driver.find_elements(*self.radio_buttons)[i].get_attribute("value") == value:
                self.driver.find_elements(*self.radio_buttons)[i].click()

    def get_selected_value(self):
        self.driver.find_element(*self.get_checked_value).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_msg).text
