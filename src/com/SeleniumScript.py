from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
# https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy
# https://www.selenium.dev/documentation/webdriver/waits/
# https://www.selenium.dev/documentation/webdriver/waits/
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected
# https://www.selenium.dev/blog/2022/bellatrix-test-automation-framework/


driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(10)
print(driver.title)
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
driver.quit()
