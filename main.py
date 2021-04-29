import os
import file_handling as file_h
import driver_handling as driver_h
import website_check as wc

websites = file_h.website_reader()
driver = driver_h.webdriver_setup()


wc.load_with_addon(driver, websites)
wc.close_driver_session(driver)

driver = driver_h.webdriver_setup()
wc.load_without_addon(driver, websites)
wc.close_driver_session(driver)





''' loading addons for firefox to use with selenium for more than one addon:

extensions = [
    'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi',
    '',
    ''
]
for extension in extensions:
driver.install_addon(extension_dir + extension, temporary=True)
'''


