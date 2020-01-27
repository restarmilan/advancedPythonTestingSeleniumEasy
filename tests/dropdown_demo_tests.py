import unittest

from ddt import ddt, file_data

from dropdown_demo_page import DropdownDemoPage
from tests.base_test import BaseTest


@ddt
class DropdownDemoTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.dropdown = DropdownDemoPage(self.driver)
        self.dropdown.navigate_to_dropdown_demo_page()

    @file_data('resources/simple_dropdown_data.json')
    def test_simple_dropdown(self, option, expected):
        dropdown = self.dropdown
        dropdown.select_an_option_from_dropdown(option)
        self.assertTrue(dropdown.get_selected_value_simple_dropdown(), expected)


if __name__ == "__main__":
    unittest.main()
