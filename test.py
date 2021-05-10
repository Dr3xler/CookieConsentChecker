import file_handling as file_h
import driver_handling as driver_h
import idcac_poc
import collect_websites as collect

websites = file_h.website_reader_cookie_websites()
driver = driver_h.webdriver_setup()

#idcac_poc.addon_check(driver, websites)

collect.generate_website_list(driver, websites)
