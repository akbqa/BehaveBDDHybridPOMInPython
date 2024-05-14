from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    logout_link_xpath = "//a[contains(text(),'Logout')]"

    def click_on_logout_link(self):
        self.click_on_element("logout_link_xpath", self.logout_link_xpath)