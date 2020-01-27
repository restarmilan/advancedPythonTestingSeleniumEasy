from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from base_page import BasePage


class DropdownDemoPage(BasePage):
    simple_dropdown = (By.XPATH, "//select[@id='select-demo']")
    selected_value_simple_dropdown = (By.XPATH, "//p[@class='selected-value']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_dropdown_demo_page(self):
        super().navigate_to("basic-select-dropdown-demo.html")

    def select_an_option_from_dropdown(self, option):
        select = Select(self.driver.find_element(*self.simple_dropdown))
        select.select_by_value(option)

    def get_selected_value_simple_dropdown(self):
        return self.driver.find_element(*self.selected_value_simple_dropdown).text
