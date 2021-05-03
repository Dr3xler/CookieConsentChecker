import os
import json
import shutil
import time

import cookie_compare


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
    """This method will load all websites with 'i don't care about cookies' preinstalled.
    Afterwards it will convert the cookies to dicts and save them locally for comparison
    Be aware that this method will delete all saved cookies"""

    print('creating dir for cookies with addon...')

    # checks if cookie dir already exists, creates an empty dir.
    if len(os.listdir('data/save/with_addon/')) != 0:
        shutil.rmtree('data/save/with_addon/')
        os.mkdir('data/save/with_addon/')

    print('saving cookies in firefox with addons ...')

    # the extension directory needs to be the one of your local machine
    extension_dir = os.getenv("HOME") + "/.mozilla/firefox/7ppp44j6.default-release/extensions/"

    driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)

    for website in websites:
        name = website.split('www.')[1]
        driver.get(website)
        driver.execute_script("return document.readyState")
        time.sleep(5)

        cookies_addons = driver.get_cookies()
        cookies_dict = {}
        cookiecount = 0

        for cookie in cookies_addons:
            cookies_dict = cookie

            print('data/save/with_addon/%s/%s_%s.json' % (name, name, cookiecount))
            print(cookies_dict)

            # creates the website dir
            if not os.path.exists('data/save/with_addon/%s/' % name):
                os.mkdir('data/save/with_addon/%s/' % name)
            # saves the cookies into the website dir
            with open('data/save/with_addon/%s/%s_%s.json' % (name, name, cookiecount), 'w') as file:
                json.dump(cookies_dict, file, sort_keys=True)

            cookiecount += 1


def load_without_addon(driver, websites):
    """This method will load all websites on a vanilla firefox version.
    Afterwards it will convert the cookies to dicts and save them locally for comparison
    Be aware that this method will delete all saved cookies"""

    print('creating dir for cookies in vanilla...')

    # checks if cookie dir already exists, creates an empty dir.
    if len(os.listdir('data/save/without_addon/')) != 0:
        shutil.rmtree('data/save/without_addon/')
        os.mkdir('data/save/without_addon')

    print('saving cookies in firefox without addons ...')

    for website in websites:
        name = website.split('www.')[1]
        driver.get(website)
        driver.execute_script("return document.readyState")
        time.sleep(5)

        cookies_vanilla = driver.get_cookies()
        cookies_dict = {}
        cookiecount = 0

        for cookie in cookies_vanilla:
            cookies_dict = cookie

            print('data/save/without_addon/%s/%s_%s.json' % (name, name, cookiecount))
            print(cookies_dict)

            # creates the website dir
            if not os.path.exists('data/save/without_addon/%s/' % name):
                os.mkdir('data/save/without_addon/%s/' % name)
            # saves the cookies into the website dir
            with open('data/save/without_addon/%s/%s_%s.json' % (name, name, cookiecount), 'w') as file:
                json.dump(cookies_dict, file, sort_keys=True)

            cookiecount += 1


def close_driver_session(driver):
    """This method will end the driver session and close all windows. Driver needs to be initialized again afterwards"""
    driver.quit()


