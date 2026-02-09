from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Cargamos la configuración para Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

# Cargamos controlador de Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Seleccionamos lenguaje
select_lenguage_en = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)
select_lenguage_en.click()

# Eliminamos el mensaje de cookies
quit_cookies_message = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "cc_btn_accept_all"))
)
quit_cookies_message.click()

duration_seconds = 60 * 5    # Quiero que el juego dure 5 minutos antes de cerrar la ventana
start_time = time.time()    # Inicializamos el tiempo para empezar a contar
while time.time() - start_time <= duration_seconds:
    try:
        # Intentamos buscar la galleta para darle click
        press_cookie = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, "bigCookie"))
        )
        press_cookie.click()
    except:
        continue

    if int(time.time() - start_time) % 5 == 0 and int(time.time() - start_time) != 0:

        try:
            # Buscamos las mejoras que podemos comprar
            upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
            if upgrades:
                # Si no tenemos una lista vacía, compraremos la mejora
                upgrades[-1].click()
            else:
                # Buscamos los productos disponibles
                products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
                if products:
                    # Compramos los productos más caros que podamos comprar
                    products[-1].click()

        except Exception as e:
            print(f"Error al comprar: {e}")

    # number_cookies = driver.find_element(By.ID, "cookies")
    # print(f"{number_cookies.get_attribute("textContent").split()[0]} cookies")

cookies_per_second = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "cookiesPerSecond"))
    )
print(cookies_per_second.get_attribute("textContent"))


