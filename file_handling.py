import json


def website_reader():
    """This method will read the websites.txt file into a list"""
    # reading txt file for websites used by selenium

    with open('data/websites', "r") as f:
        websites = f.readlines()
    websites = [x.strip() for x in websites]

    return websites

