from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configura el WebDriver (en este caso, Chrome)
driver = webdriver.Chrome()

try:
    # Abre la página web del sistema de tickets
    driver.get("http://helpdesk.caabsa.com")
    driver.save_screenshot('step1_open_website.png')  # Captura de pantalla

    # Espera hasta que el botón "Iniciar Sesión" esté presente y sea clickeable
    login_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Inicia Sesión"))
    )
    login_button.click()
    driver.save_screenshot('step2_click_login.png')  # Captura de pantalla

    # Espera hasta que el enlace "Ingresa con tu cuenta corporativa Google" esté presente y sea clickeable
    google_login_link = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Ingresa con tu cuenta corporativa Google"))
    )
    google_login_link.click()
    driver.save_screenshot('step3_click_google_login.png')  # Captura de pantalla

    # Espera a que la página de inicio de sesión de Google cargue y el campo de correo esté presente
    email_field = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys("dislas@caabsa.com.mx")
    driver.save_screenshot('step4_enter_email.png')  # Captura de pantalla

    # Haz clic en el botón "Siguiente"
    next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Siguiente')]/ancestor::button")
    next_button.click()
    driver.save_screenshot('step5_click_next.png')  # Captura de pantalla

    # Espera a que el campo de contraseña esté presente y sea clickeable
    password_field = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", password_field)
    driver.save_screenshot('step6_password_field_visible.png')  # Captura de pantalla

    time.sleep(2)  # Agrega un pequeño retraso

    # Ingresa la contraseña usando JavaScript para asegurar la interacción
    driver.execute_script("arguments[0].value = 'Di13Go94$';", password_field)
    driver.save_screenshot('step7_enter_password.png')  # Captura de pantalla

    # Haz clic en el botón "Siguiente" después de ingresar la contraseña
    next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Siguiente')]/ancestor::button")
    next_button.click()
    driver.save_screenshot('step8_click_next_after_password.png')  # Captura de pantalla

    # Verifica que no estás en la página de inicio de sesión de Google
    WebDriverWait(driver, 60).until_not(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    driver.save_screenshot('step9_logged_in.png')  # Captura de pantalla

    # Imprime la URL actual para ver si estamos en la página correcta
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    driver.save_screenshot('step10_open_ticket_page.png')  # Captura de pantalla

    # Espera hasta que el menú desplegable de "Tema de ayuda" esté presente
    form_control_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )
    select = Select(form_control_element)
    select.select_by_visible_text("Asana")  # Cambia "Asana" por el texto visible de la opción que necesites
    driver.save_screenshot('step11_select_topic.png')  # Captura de pantalla

    # Encuentra el campo de "Título" basado en la clase y tipo
    titulo_field = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='form-control' and @type='text']"))
    )
    titulo_field.send_keys("test selenium")
    driver.save_screenshot('step12_enter_title.png')  # Captura de pantalla

    # Verifica si el elemento de texto enriquecido está presente
    detalles_richtext_divs = driver.find_elements(By.XPATH, "//div[@class='redactor-styles' and @contenteditable='true']")
    if detalles_richtext_divs:
        detalles_richtext_div = detalles_richtext_divs[0]
        actions = ActionChains(driver)
        actions.move_to_element(detalles_richtext_div).click().send_keys("Pruebas tracking").perform()
        time.sleep(2)
        driver.save_screenshot('step13_enter_richtext.png')  # Captura de pantalla
    else:
        print("Elemento de texto enriquecido no encontrado, intentaremos con JavaScript.")
        script = "document.querySelector('.redactor-styles[contenteditable=\"true\"]').innerHTML = 'Pruebas tracking';"
        driver.execute_script(script)
        time.sleep(2)
        driver.save_screenshot('step13_enter_richtext_js.png')  # Captura de pantalla

    # Ahora hace clic en el botón "Crear Ticket"
    crear_ticket_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Crear Ticket']"))
    )
    crear_ticket_button.click()
    driver.save_screenshot('step14_click_create_ticket.png')  # Captura de pantalla

    # Pausa el script para que el navegador no se cierre
    input("Ticket creado, presiona Enter para cerrar el navegador...")

finally:
    # Cierra el navegador al final
    driver.quit()
