class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, route):
        base_url = "https://www.seleniumeasy.com/test/"
        self.driver.get(base_url + route)
