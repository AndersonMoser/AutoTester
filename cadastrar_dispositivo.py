from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o driver do Chrome
driver = webdriver.Chrome()

# Abrir o navegador e acessar a página
driver.get('http://10.0.1.240:4000')
driver.maximize_window()

# Identificar os campos de login
usuario = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
)
senha = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')

# Realizar login
usuario.clear()
usuario.send_keys('20237527000141')
senha.clear()
senha.send_keys('20237527000141')
senha.send_keys(Keys.ENTER)

# Aguardar até que o menu de cadastros esteja presente
menudispositivo = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'app-menu > ul > li:nth-child(3) > a'))
)
menudispositivo.click()
time.sleep(3)

# Clicar no botão "Novo" usando o texto do botão
novodispositivo = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Novo"]'))
)
novodispositivo.click()

# Identificar os campos do formulário
nome = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="name"]'))
)
tipo = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > p-dropdown > div > span'))
)


# Preenchendo os campos
nome.send_keys('CONDOMINIO SEGURANÇA FORTE')
tipo.click()

#Selecionar o tipo do dispositivo
tipo_options = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//li[span[text()="IP Controller"]]'))
)
tipo_options.click()

#Preencher url
endereçoip = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="internetProtocol"]'))

)
endereçoip.send_keys('10.0.7.123')

#Preencher usuário e senha 
usuariodispositivo = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="user"]'))
)
senhadispositivo = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')

usuariodispositivo.send_keys('siam')
senhadispositivo.send_keys('siam')

#Mover barra de rolar
driver.execute_script("window.scrollTo(0, -500);")

#Aguardar a barra rolar
time.sleep(5)

#Validar conexão
validarconexao = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Validar conexão"]'))
)
validarconexao.click()

#Aguardar realizar a conexão
time.sleep(15)
gravardispositivo = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Gravar"]'))
    )
gravardispositivo.click()

try:
        # Esperar pela mensagem de sucesso
        cadastro_salvo = WebDriverWait(driver, 60).until(
           EC.element_to_be_clickable((By.XPATH, '//span[text()="Registro gravado com sucesso!"]'))
        )
        # Verificar o texto da mensagem de sucesso
        assert "Registro gravado com sucesso!" in cadastro_salvo.text
        print("Mensagem de cadastro realizado com sucesso!")
except Exception as e:
        print("A mensagem não foi encontrada ou o texto não corresponde:", str(e))

