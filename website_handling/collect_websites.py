import os
from sys import platform
from pathlib import Path


def generate_website_list(driver, websites):
    """This method will load websites from a file and adds them to a new list if user input is y"""

    cookie_exists_list = []
    list_count = 0
    for website in websites:
        name = website.split('www.')[1]
        try:
            driver.get(website)
        except:
            continue

        driver.execute_script("return document.readyState")

        choice = input('save website?')
        if choice == "y":
            cookie_exists_list.append(website)
            list_count += 1
            print(list_count)

        if choice == "n":
            continue
        if choice == "stop":
            break
        if choice == "exit":
            break
        else:
            continue

    cookie_websites = open("data/cookie_websites.txt", "w")

    for line in cookie_exists_list:
        cookie_websites.write(line + "\n")

    cookie_websites.close()


def generate_success_list(driver, websites):
    """This method will load websites with addon and adds them to a new list if user input is y"""

    cookie_exists_list = []
    list_count = 0

    print(platform)
    # the extension directory needs to be the one of your local machine
    #linux
    if platform == "linux":
        extension_dir = os.getenv("HOME") + "/.mozilla/firefox/7ppp44j6.default-release/extensions/"
        driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)
    #windows
    if platform == "win32":
        extension_dir = str(Path.home()) + "/AppData/Roaming/Mozilla/Firefox/Profiles/shdzeteb.default-release/extensions/"
        print(extension_dir)
        driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)

    for website in websites:
        name = website.split('www.')[1]
        try:
            driver.get(website)
        except:
            continue

        driver.execute_script("return document.readyState")

        choice = input('save website?')
        if choice == "y":
            cookie_exists_list.append(website)
            list_count += 1
            print(list_count)

        if choice == "n":
            continue
        if choice == "stop":
            break
        if choice == "exit":
            break
        else:
            continue

    cookie_websites = open("data/cookie_addon_success.txt", "w")

    for line in cookie_exists_list:
        cookie_websites.write(line + "\n")

    cookie_websites.close()
