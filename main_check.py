import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# the extension directory needs to be the one of your local machine
extension_dir = os.getenv("HOME") + "/.mozilla/firefox/7ppp44j6.default-release/extensions/"

# loading the webdriver for selenium
driver = webdriver.Firefox(executable_path=r"webdriver/geckodriver")

''' loading addons for firefox to use with selenium for more than one addon:

extensions = [
    'hjid1-KKzOGWgsW3Ao4Q@jetpack.xpi'
]
for extension in extensions:
driver.install_addon(extension_dir + extension, temporary=True)
'''

driver.install_addon(extension_dir + 'jid1-KKzOGWgsW3Ao4Q@jetpack.xpi', temporary=True)


driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()
