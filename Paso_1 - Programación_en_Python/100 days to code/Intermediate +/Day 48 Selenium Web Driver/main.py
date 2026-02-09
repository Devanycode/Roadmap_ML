from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()    # Creamos un objeto de configuración para Chrome


# Hago esto para poder abrir Amazon con el código
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")

chrome_options.add_experimental_option("detach", True)    # Sirve para que la ventana se quede abierta y no se cierre de inmediato

driver = webdriver.Chrome(options=chrome_options)    # Se hace esto para decirle a Selenium con qué controlador trabajar
driver.get("https://www.amazon.com/-/es/Micr%C3%B3fono-cardioide-din%C3%A1mico-Shure-SM57-LC/dp/B0000AQRST/ref=sr_1_6?sr=8-6")

# Hacemos esto para obtener el valor del precio, sin caer en errores de buscar los datos antes de encontrarlos
price_COP = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-offscreen")))
price_real = price_COP.get_attribute("textContent").split("COP")[1]    # Para sólo incluir el precio
print(price_real)


# driver.close()    # Esta función cerrará únicamente la ventana que estamos seleccionando
driver.quit()    # Cerrará todas las ventanas que hayan abiertas, cerrando todo el programa (el navegador)