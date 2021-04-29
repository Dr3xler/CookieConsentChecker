from selenium import webdriver


def webdriver_setup():
    """This method will load the firefox webdriver"""
    # loading the webdriver for selenium
    driver = webdriver.Firefox(executable_path=r"webdriver/geckodriver")

    return driver
