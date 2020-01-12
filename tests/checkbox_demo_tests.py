import unittest

from ddt import ddt, unpack, data

from checkbox_demo_page import CheckboxDemoPage
from tests.base_test import BaseTest


@ddt
class CheckboxDemoTests(BaseTest):

    @unpack
    @data({"inputs": [0, 0, 0, 0], "expected": "Check All"},
          {"inputs": [1, 0, 0, 0], "expected": "Check All"},
          {"inputs": [1, 1, 0, 0], "expected": "Check All"},
          {"inputs": [1, 1, 1, 0], "expected": "Check All"},
          {"inputs": [1, 1, 1, 1], "expected": "Uncheck All"})
    def test_multiple_checkbox(self, inputs, expected):
        checkbox = CheckboxDemoPage(self.driver)
        checkbox.navigate_to_checkbox_demo_page()
        checkbox.click_on_multiple_checkbox(inputs)
        self.assertEqual(checkbox.get_checkbox_button_value(), expected)


if __name__ == "__main__":
    unittest.main()
