import os
import time
import json
import sys
import struct
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def addon_check(driver, websites):
    """This method will load all websites with 'i don't care about cookies' preinstalled.
    Afterwards it will convert the cookies to dicts and save them locally for comparison
    Be aware that this method will delete all saved cookies"""

    # the extension directory needs to be the one of your local machine
    extension_dir = os.getenv("HOME") + "/.mozilla/firefox/7ppp44j6.default-release/extensions/"
    driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)
    success_counter = 0
    for website in websites:
        name = website.split('www.')[1]
        driver.get(website)
        driver.execute_script("return document.readyState")

        # time.sleep(5)
        try:
            read_popup(driver)

        except:
            print('none found')


        # if driver.execute_script("return chrome.notifications.getAll()"):
        #    success_counter += 1

    # print(success_counter)
    # return success_counter

# Read a message from stdin and decode it.


def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message)


def read_popup(driver):
    alert = driver.switch_to.alert()
    alert_text = alert.text
    # validate the alert text
    # alert.accept()
    print(alert_text)
