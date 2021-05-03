import file_handling as file_h
import driver_handling as driver_h
import website_check as wc
import cookie_compare


websites = file_h.website_reader()
driver = driver_h.webdriver_setup()





try:
    wc.load_with_addon(driver, websites)
except:
    print('ERROR: IN FIREFOX USAGE WITH ADDONS')
finally:
    wc.close_driver_session(driver)


# driver need to be reloaded because we need a new session without addons
driver = driver_h.webdriver_setup()

try:
    wc.load_without_addon(driver, websites)
except:
    print('ERROR: IN VANILLA FIREFOX VERSION')
finally:
    wc.close_driver_session(driver)

cookie_compare.compare(websites)



