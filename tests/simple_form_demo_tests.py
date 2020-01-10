from tests.base_test import BaseTest
from simple_form_demo_page import SimpleFormDemoPage


class SimpleFormDemoTests(BaseTest):

    def test_try_it(self):
        simple = SimpleFormDemoPage(self.driver)
        simple.navigate_to_simple_demo_form_page()
        simple.set_user_input_to_simple_input_field("test-message")
        simple.click_on_confirmation_button()
        self.assertEqual(simple.get_user_message(), "test-message")
