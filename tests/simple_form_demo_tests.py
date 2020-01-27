import unittest

from ddt import file_data, ddt

from simple_form_demo_page import SimpleFormDemoPage
from tests.base_test import BaseTest


@ddt
class SimpleFormDemoTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.simple = SimpleFormDemoPage(self.driver)
        self.simple.navigate_to_simple_demo_form_page()

    @file_data('resources/simple_input_message.json')
    def test_simple_input_field(self, message, expected):
        simple = self.simple
        simple.set_user_input_to_simple_input_field(message)
        simple.click_on_confirmation_button()
        self.assertEqual(simple.get_user_message(), expected)

    @file_data('resources/double_input_fields_data.json')
    def test_double_input_fields(self, value1, value2, expected):
        simple = self.simple
        simple.set_double_user_input(value1, value2)
        simple.add_values()
        self.assertEqual(simple.get_added_values(), expected)


if __name__ == "__main__":
    unittest.main()
