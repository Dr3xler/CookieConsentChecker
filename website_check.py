import os

# TODO: Add ability to save cookies to both methods


def load_with_addon(driver, websites):
    """This method will load all websites with 'i don't care about cookies' preinstalled."""
    print('saving cookies in firefox with addons ...')


    # the extension directory needs to be the one of your local machine
    extension_dir = os.getenv("HOME") + "/.mozilla/firefox/7ppp44j6.default-release/extensions/"

    driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)

    for website in websites:
        driver.get(website)



def load_without_addon(driver, websites):
    """This method will load all websites on a vanilla firefox version"""

    print('saving cookies in firefox without addons ...')

    for website in websites:
        driver.get(website)


def close_driver_session(driver):
    driver.quit()
