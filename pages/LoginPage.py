from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utilities import ConfigReader


class LoginPage(BasePage):

    def __init__(self, driver, email=None, password=None):
        super().__init__(driver)
        self.email = email if email else ConfigReader.read_configuration("basic info", "email")
        self.password = password if password else ConfigReader.read_configuration("basic info", "password")

    email_address_field_id = "Email"
    password_field_id = "Password"
    login_button_xpath = "//button[@type='submit']"
    warning_message_xpath = "//div[@class='message-error validation-summary-errors']"

    def enter_email_address(self, email=None):
        email = email if email else self.email
        self.type_into_element("email_address_field_id", self.email_address_field_id, email)

    def enter_password(self, password=None):
        password = password if password else self.password
        self.type_into_element("password_field_id", self.password_field_id, password)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def display_status_for_warning_message(self, expected_warning_text):
        return self.retrieved_element_text_contains("warning_message_xpath", self.warning_message_xpath, expected_warning_text)

    def wait_for_warning_message(self):
        return self.wait_for_element(By.XPATH, self.warning_message_xpath)
