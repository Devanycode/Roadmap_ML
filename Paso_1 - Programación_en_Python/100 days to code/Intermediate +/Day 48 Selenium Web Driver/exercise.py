from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

menu = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last .shrubbery .menu li a")
time = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last .shrubbery .menu time")
menu_list = [element.get_attribute("textContent") for element in menu]
time_list = [element.get_attribute("textContent") for element in time]
print(time_list)
print(menu_list)

driver.close()