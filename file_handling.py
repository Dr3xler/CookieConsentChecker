import json


def website_reader():
    """This method will read the websites.txt file into a list"""
    # reading txt file for websites used by selenium

    with open('data/websites', "r") as f:
        websites = f.readlines()
    websites = [x.strip() for x in websites]

    return websites


def website_reader_csv():
    """This method will read the websites.txt file into a list"""
    # reading txt file for websites used by selenium
    websites2 = []

    with open('data/TOP10.000.txt', "r") as f:
        websites = f.readlines()
    websites = [x.strip() for x in websites]

    for website in websites:
        website2 = "http://www." + website
        websites2.append(website2)
    return websites2
