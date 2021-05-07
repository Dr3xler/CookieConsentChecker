import os
import time


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

        if driver.execute_script("return chrome.notifications.getAll()"):
            success_counter += 1

    print(success_counter)
    return success_counter
