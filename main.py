import file_handling as file_h
import driver_handling as driver_h
import website_check as wc

websites = file_h.website_reader()
driver = driver_h.webdriver_setup()

try:
    wc.load_with_addon(driver, websites)
except:
    print('something went wrong')
finally:
    wc.close_driver_session(driver)


# driver need to be reloaded because we need a new session without addons
driver = driver_h.webdriver_setup()

try:
    wc.load_without_addon(driver, websites)
except:
    print('something went wrong')
finally:
    wc.close_driver_session(driver)




