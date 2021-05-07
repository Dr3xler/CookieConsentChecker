import file_handling as file_h
import driver_handling as driver_h
import idcac_poc


websites = file_h.website_reader()
driver = driver_h.webdriver_setup()

idcac_poc.addon_check(driver, websites)
