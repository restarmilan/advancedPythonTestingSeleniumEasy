from ddt import file_data, ddt

from simple_form_demo_page import SimpleFormDemoPage
from tests.base_test import BaseTest


@ddt
class SimpleFormDemoTests(BaseTest):

    @file_data('resources/simple_input_message.json')
    def test_simple_input_field(self, message, expected):
        simple = SimpleFormDemoPage(self.driver)
        simple.navigate_to_simple_demo_form_page()
        simple.set_user_input_to_simple_input_field(message)
        simple.click_on_confirmation_button()
        self.assertEqual(simple.get_user_message(), expected)


if __name__ == "__main__":
    # unittest.main()
    tc = SimpleFormDemoTests()
    super().run_single(tc, tc.test_simple_input_field)