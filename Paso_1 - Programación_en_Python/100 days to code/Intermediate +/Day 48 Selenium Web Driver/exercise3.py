from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
first_name_input.send_keys("Devany")

last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("Rincón")

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("userpython@py.com")

sing_up_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
sing_up_button.click()

