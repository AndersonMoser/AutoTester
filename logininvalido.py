from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar o navegador
driver = webdriver.Chrome()

# Navegar para a página de login
driver.get('http://10.0.1.240:4000')
driver.maximize_window()

# Localizar os campos de entrada
usuario = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="username"]')
senha = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')

# Inserir um usuário inválido
usuario.clear()
usuario.send_keys('usuario_invalido')
senha.clear()
senha.send_keys('senha_invalida')
senha.send_keys(Keys.ENTER)

# Esperar pela mensagem de erro e validar
try:
    # Ajuste o seletor CSS de acordo com a estrutura HTML da sua página
    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > app-root > app-auth-layout > ng-component > p-confirmdialog > div > div > div.p-dialog-content.ng-tns-c140-0'))
    )
    # Verificar o texto da mensagem de erro
    assert "Usuário e/ou senha inválidos" in mensagem_erro.text
    print("Mensagem de erro validada com sucesso!")
except Exception as e:
    print("A mensagem de erro não foi encontrada ou o texto não corresponde.")
    
finally:()
