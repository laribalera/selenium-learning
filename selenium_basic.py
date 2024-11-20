from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# webdriver - manipula o navegdor. Passar como método o navegador a ser utilizado
driver = webdriver.Firefox()

# a partir da variavel driver, get define o caminho a acessar
driver.get("https://google.com")

# coletando titulo da pagina e url
title = driver.title
url = driver.current_url

print("Acessando: ", title)
print("URL: ", url)

# procura elemento pelo atributo name
element = driver.find_element(By.NAME, 'q')

# insere um valor no elemento e faz a açao de enter
element.send_keys('Selenium Docs')
element.send_keys(Keys.RETURN)

#print(element)

time.sleep(3)

# encerrando fluxo
driver.quit()
