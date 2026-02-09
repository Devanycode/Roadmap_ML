from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(f"the number of articles is: {article_count.get_attribute("textContent")}")

# Esta es la forma de abrir un link de forma sencilla sólo con escribir el nombre del link
# all_portals = driver.find_element(By.LINK_TEXT, "Reference desk")
# all_portals.click()

search = driver.find_element(By.NAME, "search")    # Acceder al bloque de input para escribir algo y buscar 
search.send_keys("Python")    # Para entregarle un texto a la barra de búsqueda (input)
search.send_keys(Keys.ENTER)    # Para presionar el botón enter