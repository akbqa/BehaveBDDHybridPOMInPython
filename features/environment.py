from utilities import ConfigReader
from selenium import webdriver


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()
