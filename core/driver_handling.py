from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver


def webdriver_setup():
    """This method will load the firefox webdriver"""
    # loading the webdriver for selenium
    driver = webdriver.Firefox(executable_path=r"../webdriver/geckodriver")

    return driver

