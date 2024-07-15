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

# Aguardar até que o menu de cadastros esteja presente
menucadastros = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'app-menu > ul > li:nth-child(2) > a'))
)
menucadastros.click()

# Aguardar até que o submenu de empresas esteja presente e clicar nele
submenuempresas = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/registration/companys"]'))
)
submenuempresas.click()

# Tentar localizar e clicar no botão "Novo" usando o texto do botão
novoempresa = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Novo"]'))
)
novoempresa.click()

# Identificar os campos do formulário
razaosocial = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="corporateName"]'))
)
cnpj = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="document"]')
emailempresa = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="email"]')
adicionaremailempresa = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(9) > div:nth-child(3) > button')

# Preenchendo os campos
razaosocial.send_keys('SEGURANÇA FORTE')
cnpj.send_keys('63647511000110')
emailempresa.send_keys('testesoftware2@siam.ind.br')
adicionaremailempresa.click()

# Selecionar estado
uf = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(5) > div.p-col-12.p-md-12 > div:nth-child(2) > p-dropdown > div > span'))
)
uf.click()
uf_option = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'p-dropdownitem:nth-child(24) > li > span'))
)
uf_option.click()

# Adicione qualquer ação adicional necessária aqui, como salvar o formulário

# Aguarde alguns segundos antes de fechar o navegador (opcional)
time.sleep(5)

# Fechar o navegador
driver.quit()