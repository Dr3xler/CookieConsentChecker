import time
import shutil
import os
import json


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
