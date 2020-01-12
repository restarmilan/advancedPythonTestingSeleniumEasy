from base_page import BasePage


class RadioButtonDemoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_radio_buttons_demo_page(self):
        super().navigate_to("basic-radiobutton-demo.html")
