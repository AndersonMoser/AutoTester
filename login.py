from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o driver do Chrome
driver = webdriver.Chrome()

# Abrir o navegador e acessar a página
driver.get('http://10.0.2.193:4000')
driver.maximize_window()

# Identificar os campos de login
usuario = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
)
senha = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')

# Realizar login
usuario.clear()
usuario.send_keys('05573761900')
senha.clear()
senha.send_keys('791536aA')
senha.send_keys(Keys.ENTER)

# Aguarde alguns segundos antes de fechar o navegador (opcional)
time.sleep(5)