from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

ACCOUNT_EMAIL = "devany@test.com"
ACCOUNT_PASSWORD = "passwordTest"
GYM_URL = "https://appbrewery.github.io/gym/"

# Configuro las opciones con las que 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

# Creo la carpeta de perfil de chrome para abrirlo siempre con los mismos datos 
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")    # Carpeta con perfil
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")    # Hacemos que Selenium abra chrome con ese perfil 

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 5)


def retry(condition, retries=3, description=None):
    """Reintenta un wait específico hasta 'retries' veces si hay Timeout."""
    last_exception = None
    for i in range(retries):
        if description:
            print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return wait.until(condition)  # Ejecuta el wait
        except TimeoutException as e:
            last_exception = e
            if i < retries - 1:
                print(f"Timeout in {description}, retrying after 1s...")
                time.sleep(1)  # Espera antes de reintentar
            else:
                raise last_exception  # Lanza solo al final
                
def login():
    """Iniciamos sesión en el sitio web"""
    # Presionamos el botón de iniciar sesión 
    login_button = retry(
        EC.element_to_be_clickable((By.ID, "login-button")),
        description="botón de login"
    )
    login_button.click()

    # INICIAR SESIÓN
    # Escribimos el Email
    email_input = retry(
        EC.presence_of_element_located((By.ID, "email-input")),
        description="input de email"
    )
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    # Escribimos la contraseña
    password_input = retry(
        EC.presence_of_element_located((By.ID, "password-input")),
        description="input de password"
    )
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    # Concretamos el inicio de sesión
    submit_login = retry(
        EC.element_to_be_clickable((By.ID, "submit-button")),
        description="botón de submit"
    )
    submit_login.click()
    if wait.until(EC.presence_of_element_located((By.ID, "error-message"))): 
        retry(
        EC.element_to_be_clickable((By.ID, "submit-button")),
        description="botón de submit")

    # Esperamos a que la página principal cargue
    retry(
        EC.presence_of_element_located((By.ID, "schedule-page")),
        description="página de schedule"
    )

login()



# Encontrando los horarios de las clases del jueves
thursday_abbr = "thu"
thursday_time_classes = driver.find_elements(By.CSS_SELECTOR, f"div[id^='day-group'][id*='{thursday_abbr}'] p[id^='class-time-']")
thursday_time_list = [element.text.strip() for element in thursday_time_classes]

# Encontrando los horarios de las clases del martes
tuesday_abbr = "tue"
tuesday_time_classes = driver.find_elements(By.CSS_SELECTOR, f"div[id^='day-group'][id*='{tuesday_abbr}'] p[id^='class-time-']")    
tuesday_time_list = [element.text.strip() for element in tuesday_time_classes]

# Escribimos la hora que queremos en el formato que lo entrega el HTML [TIME: x:xx PM]
request_time = "Time: 6:00 PM"

# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0

def booking_clases(day_time_list, selenium_list_time_classes, request_time, day_abbreviation):
    global booked_count, waitlist_count, already_booked_count

    if request_time in day_time_list:
        hour_index = day_time_list.index(request_time)
        full_id = selenium_list_time_classes[hour_index].get_attribute("id")
        id_date = full_id.split("class-time-")[-1]   # Capturamos la fecha y hora para hacer la búsqueda del botón correspondiente
        # Botón para agendar clase
        button_class = retry(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"button[id^='book-button'][id$='{id_date}']")),  # Cambié a clickable para robustez
            description=f"botón de book para {id_date}"
        )
        # Nombre de la clase
        class_name = retry(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"h3[id^='class-name'][id$='{id_date}']")),
            description=f"nombre de clase para {id_date}"
        )
        # Fecha de la clase
        class_date = retry(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"h2[id^='day-title'][id*='{day_abbreviation}']")),
            description=f"título de día para {day_abbreviation}"
        )

        # Si el botón aún no está agendado entonces le daremos click para agendarlo
        if button_class.text == "Book Class".strip():
            # Book the class
            button_class.click()
            already_booked_count += 1
            print(f"✓ Successfully booked: {class_name.text} on {class_date.text}")
        elif button_class.text == "Booked":
            booked_count += 1
            print(f"✓ Already {button_class.text}, {class_name.text} on {class_date.text}")
            
        elif button_class.text == "Join Waitlist".strip():
            # Join waitlist
            button_class.click()
            already_booked_count += 1
            print(f"✓ Joined {button_class.text}, {class_name.text} on {class_date.text}")
        elif button_class.text == "Waitlisted":
            waitlist_count += 1
            print(f"✓ Already {button_class.text}, {class_name.text} on {class_date.text}")

        return button_class.text, class_name.text, class_date.text
    else:
        print(f"Sorry, there are no classes on {day_abbreviation} at {request_time}")


button_class_tue, class_name_tue, class_date_tue = booking_clases(
    tuesday_time_list, tuesday_time_classes, request_time, tuesday_abbr
    )

button_class_thu, class_name_thu, class_date_thu = booking_clases(
    thursday_time_list, thursday_time_classes, request_time, thursday_abbr
    )

# Listas con los datos
button_classes_list = [button_class_tue, button_class_thu]
class_names_list = [class_name_tue, class_name_thu]
class_dates_list = [class_date_tue, class_date_thu]

total_booked_waitlist_classes = booked_count + waitlist_count + already_booked_count
# print summary (todo esto es para la hora solicitada)
# print("\n BOOKING SUMMARY ---\n")
# print(f"Classes booked: {booked_count}")
# print(f"Waitlists joined: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday & Thursday 6pm classes processed: {total_booked_waitlist_classes}")

"""
print("\n--- DETAILED CLASS LIST ---")
for button_class, class_name, class_date in zip(button_classes_list, class_names_list, class_dates_list):
    if button_class == "Booked":
        print(f"• [New Booking] {class_name} on {class_date}")
    elif button_class == "Wailisted":
        print(f"• [New Waitlist] {class_name} on {class_date}")
"""
# Clickeamos en "My Bookings" para ver nuestras reservas actuales
my_bookings_page = wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link")))
my_bookings_page.click()
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

verification_count = 0
# Vamos a verificar si reservamos las clases de forma exitosa y cargaron en la página
try:
    booking_classes = driver.find_elements(By.CSS_SELECTOR, "[id*='booking-class-name']")
    for class_ in booking_classes:
        print(f"✓ verified: {class_.text}")
        verification_count += 1
except SessionNotCreatedException:
    print("You have no classes booked.")

try:
    waitlist_classes = driver.find_elements(By.CSS_SELECTOR, "div h3[id*='waitlist-class-name']")
    for class_ in waitlist_classes:
        print(f"✓ verified: {class_.text}")
        verification_count += 1
except SessionNotCreatedException:
    print("You have no classes on the waitlist.")

# Imprimimos los resultados de la verificación
print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked_waitlist_classes} bookings")
print(f"Found: {verification_count} bookings")

if total_booked_waitlist_classes == verification_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {verification_count - already_booked_count} bookings")


