from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'C:\path\to\chrome\driver')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://coinmarketcap.com/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, "Full Xpath").text #Full Xpath is not actually "Full Xpath" this is just a placeholder
    return element

print(main())
