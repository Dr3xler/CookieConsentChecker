from selenium import webdriver
from sys import platform
from selenium.webdriver.firefox.webdriver import WebDriver


def webdriver_setup():
    """This method will load the firefox webdriver"""

    # linux
    # loading the webdriver for selenium
    if platform == "linux":
        driver = webdriver.Firefox(executable_path=r"webdriver/geckodriver")
        return driver
    if platform == "win32":
        driver = webdriver.Firefox(executable_path=r"webdriver/geckodriver.exe")
        return driver

