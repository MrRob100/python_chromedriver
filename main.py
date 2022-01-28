from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()

if "GOOGLE_CHROME_BIN" in os.environ:
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

if "HROMEDRIVER_PATH" in os.environ:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
else:
    driver = webdriver.Chrome()

driver.get("https://www.degiro.co.uk")

print(driver.page_source)
