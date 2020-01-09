from base_page import BasePage


class SimpleFormDemoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_simple_demo_form_page(self):
        super().navigate_to("basic-first-form-demo.html")

