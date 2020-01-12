import unittest

from ddt import ddt, unpack, data

from radio_button_demo_page import RadioButtonDemoPage
from tests.base_test import BaseTest


@ddt
class RadioButtonDemoTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.radio = RadioButtonDemoPage(self.driver)
        self.radio.navigate_to_radio_buttons_demo_page()

    @unpack
    @data({"value": "Male", "expected": "Radio button 'Male' is checked"},
          {"value": "Female", "expected": "Radio button 'Female' is checked"})
    def test_simple_radio_button_demo(self, value, expected):
        radio = self.radio
        radio.click_simple_radio_buttons(value)
        radio.get_selected_value()
        self.assertEqual(radio.get_confirmation_message(), expected)


if __name__ == "__main__":
    unittest.main()
