import json
import os


def compare(websites):

    different_cookies_count = 0

    print('-----------')
    print('comparison :')
    print('-----------')

    for website in websites:
        count = 0
        domain_name = website.split('www.')[1]
        each_domain_cookies = os.listdir("data/save/with_addon/%s/" % domain_name)

        try:
            for cookie in each_domain_cookies:

                with open('data/save/with_addon/%s/%s_%s.json' % (domain_name, domain_name, count), 'r') as fp:
                    json_file_addon = json.load(fp)
                    print(json_file_addon)

                with open('data/save/without_addon/%s/%s_%s.json' % (domain_name, domain_name, count), 'r') as fp:
                    json_file_vanilla = json.load(fp)
                    print(json_file_vanilla)

                # that would mean the website does not change cookies if cookie consent message is accepted
                if json_file_addon == json_file_vanilla:
                    different_cookies_count += 1

                count += 1

                print('---')
        except:
            print(IOError)
            print('---')




    print('---------------------------------------')
    print('%s cookie(s) is/are the same as before' % different_cookies_count)
    print('---------------------------------------')






