
from selenium import webdriver

option = webdriver.FirefoxOptions() 
option.add_argument("--headless")
option.add_argument("--no-sandbox")
driver = webdriver.Firefox(options=option)
driver.delete_all_cookies()
driver.implicitly_wait(13)
print('go ')
driver.get("https://snapinsta.app/")
driver.quit()
print('fin')