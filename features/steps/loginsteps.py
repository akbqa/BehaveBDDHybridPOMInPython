import time

from behave import *
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from utilities import RandomDataGenerator


@given('I navigate to login page')
def navigate_to_login_screen(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.verify_page_title("Your store. Login")


@when(u'I enter valid email and valid password')
def enter_valid_email_and_valid_password(context):
    context.login_page.enter_email_address()
    context.login_page.enter_password()


@when(u'I click on login button')
def click_on_login_button(context):
    context.login_page.click_on_login_button()


@then(u'I should get logged in')
def verify_logged_in_successfully(context):
    assert context.login_page.verify_page_title("Dashboard / nopCommerce administration")


@when(u'I enter invalid email and valid password into the fields')
def enter_invalid_email_and_valid_password(context):
    invalid_email = RandomDataGenerator.get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    print("Invalid Email: ",invalid_email)
    context.login_page.enter_password()


@then(u'I should get a proper warning message')
def verify_warning_message(context):
    context.login_page.wait_for_warning_message()
    assert context.login_page.display_status_for_warning_message("Login was unsuccessful. Please correct the errors and try again.\nNo customer account found")
