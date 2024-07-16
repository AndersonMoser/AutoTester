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
menucadastros = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'app-menu > ul > li:nth-child(2) > a'))
)
menucadastros.click()

# Aguardar até que o submenu de empresas esteja presente e clicar nele
submenuusuario = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/registration/users"]'))
)
submenuusuario.click()
time.sleep(5)

# Clicar no botão "Novo" usando o texto do botão
novousuario = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Novo"]'))
)
novousuario.click()

# Identificar os campos do formulário
nome = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="name"]'))
)

# Preenchendo os campos
nome.send_keys('SEGURANÇA FORTE')

# Selecionar classe de usuario
classeusuario = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > app-auto-complete > p-autocomplete > span > button > span.p-button-icon.pi.pi-chevron-down'))
)
classeusuario.click()
classeusuario_option = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#pr_id_6_list > li:nth-child(1)'))
)
classeusuario_option.click()

# Selecionar marcador
marcador = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(8) > div.p-formgroup-inline > div.p-col-10.p-col-nogutter > app-auto-complete > p-autocomplete > span > button'))
        )
marcador.click()

marcador_option = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#pr_id_7_list > li:nth-child(1)'))
        )
marcador_option.click()

# Selecionar tipo de chave
tipodechave = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(20) > div:nth-child(1) > div.p-formgroup-inline > div.p-col-10.p-col-nogutter > app-auto-complete > p-autocomplete > span > button'))
)
tipodechave.click()
tipodechave_option = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#pr_id_9_list > li:nth-child(9)'))
)
tipodechave_option.click()

# Selecionar marcador
marcador = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(3) > div:nth-child(8) > div.p-formgroup-inline > div.p-col-10.p-col-nogutter > app-auto-complete > p-autocomplete > span > button'))
        )
marcador.click()

marcador_option = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#pr_id_7_list > li:nth-child(1)'))
        )
marcador_option.click()

# Anexar imagem 
anexarimagem = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
)
# Caminho do arquivo
caminho_do_arquivo = r'C:\Users\anderson.moser\Pictures\imagens rosto\FACIAS SIAM\0000000001.jpg'

# Enviar o caminho do arquivo para o input do tipo file
anexarimagem.send_keys(caminho_do_arquivo)

# Adicione qualquer ação adicional necessária aqui, como salvar o formulário teste commit


