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

    @staticmethod
    def click_to_radio_button(elements1, value1, elements2=None, value2=None):
        for i in range(len(elements1)):
            if elements1[i].get_attribute("value") == value1:
                elements1[i].click()
        if value2 is not None and elements2 is not None:
            for i in range(len(elements2)):
                if elements2[i].get_attribute("value") == value2:
                    elements2[i].click()

    def click_simple_radio_buttons(self, value):
        self.click_to_radio_button(self.driver.find_elements(*self.radio_buttons), value)

    def get_selected_value(self):
        self.driver.find_element(*self.get_checked_value).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_msg).text
