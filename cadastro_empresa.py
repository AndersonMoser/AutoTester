from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o driver do Chrome
driver = webdriver.Chrome()

# Função para realizar login
def login(driver):
    driver.get('http://173.212.231.29:4002')
    driver.maximize_window()
    
    usuario = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="username"]'))
    )
    senha = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
    
    usuario.send_keys('09405185000199')
    senha.send_keys('siam')
    senha.send_keys(Keys.ENTER)

# Função para acessar o menu de cadastros
def acessar_menu_cadastros(driver):
    menucadastros = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'app-menu > ul > li:nth-child(2) > a'))
    )
    menucadastros.click()
    
    submenuempresas = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/registration/companys"]'))
    )
    submenuempresas.click()
    time.sleep(5)

# Função para criar uma nova empresa
def criar_nova_empresa(driver):
    novoempresa = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Novo"]'))
    )
    novoempresa.click()

    uf = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(5) > div.p-col-12.p-md-12 > div:nth-child(2) > p-dropdown > div > span'))
    )
    uf.click()
    uf_option = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.p-dropdown-items-wrapper.ng-tns-c64-43 > ul > p-dropdownitem:nth-child(24) > li'))
    )
    uf_option.click()

    razaosocial = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="corporateName"]'))
    )
    cnpj = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="document"]')
    emailempresa = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="email"]')
    adicionaremailempresa = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(9) > div:nth-child(3) > button')
    
    # Preenchendo os campos
    razaosocial.send_keys('SEGURANÇA FORTE')
    cnpj.send_keys('20237527000141')
    emailempresa.send_keys('testesoftware2@siam.ind.br')
    adicionaremailempresa.click()

# Função para gravar empresa
def gravar_empresa(driver):
    gravarempresa = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Gravar"]'))
    )
    gravarempresa.click()

    try:
        # Esperar pela mensagem de sucesso
        cadastro_salvo = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > app-root > app-content-layout > div > div.layout-main > div > p-messages > div > div > div > span.p-message-summary.ng-tns-c124-2.ng-star-inserted'))
        )
        # Verificar o texto da mensagem de sucesso
        assert "Registro gravado com sucesso!" in cadastro_salvo.text
        print("Mensagem de cadastro realizado com sucesso!")
    except Exception as e:
        print("A mensagem não foi encontrada ou o texto não corresponde:", str(e))

# Execução do script
try:
    login(driver)
    acessar_menu_cadastros(driver)
    criar_nova_empresa(driver)
    gravar_empresa(driver)
finally:
    # Fechar o navegador
    driver.quit()
