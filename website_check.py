import os
import json


# TODO: Add ability to save cookies to both methods
# TODO: Maybe save cookies to global variable to compare them in another function without saving them?


''' 
loading more than one addon for firefox to use with selenium:

extensions = [
    'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi',
    '',
    ''
]
for extension in extensions:
driver.install_addon(extension_dir + extension, temporary=True)
'''


def load_with_addon(driver, websites):
    """This method will load all websites with 'i don't care about cookies' preinstalled."""

    print('saving cookies in firefox with addons ...')

    # the extension directory needs to be the one of your local machine
    extension_dir = os.getenv("HOME") + "/.mozilla/firefox/7ppp44j6.default-release/extensions/"

    driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)

    for website in websites:
        name = website + ''
        driver.get(website)

        #TODO: list of dicts. check if dicts possible and how to json this.
        cookies_addons = driver.get_cookies()
        cookies_dict = {}
        i = 0
        cookiecount = 0

        #TODO: like this, it only saves the first value "title" and not the value inside "title". Add saving the information.
        # needs something like for cookie in cookie_addons:
        #                           for key, value in cookie:
        #                               cookies_dict[key] = value
        for cookie in cookies_addons:
            for value in cookie:
                cookies_dict[i] = value
                i += 1



            # cookies_dict[cookie['name']] = cookie['value']

            with open('test.txt', 'w') as file:
                json.dump(cookies_dict, file)
            cookiecount += 1

        # with open('data/save/with_addon/' + website + '.json', 'w') as fp:
        #    json.dump(cookies, fp, sort_keys=True, indent=4)
        print(cookies_addons)


def load_without_addon(driver, websites):
    """This method will load all websites on a vanilla firefox version"""

    print('saving cookies in firefox without addons ...')

    for website in websites:
        driver.get(website)
        cookies_vanilla = driver.get_cookies()

        print(cookies_vanilla)


def close_driver_session(driver):
    """This method will end the driver session and close all windows. Driver needs to be initialized again afterwards"""
    driver.quit()


# to load json file
# with open('data.json', 'r') as fp:
#     data = json.load(fp)
