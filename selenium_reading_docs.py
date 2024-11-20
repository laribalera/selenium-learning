from selenium import webdriver 
from selenium.webdriver.common.by import By
import openai
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# apikey
openai.api_key = "OPENAI_API_KEY"

# starta o webdriver
driver = webdriver.Firefox()

# url pra acessar
url = driver.get('https://g1.globo.com/')
print("Acessando: ", driver.title)
time.sleep(3)

# wait pro elemento ficar clicavel
wait = WebDriverWait(driver, 10)
news_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".feed-post-link")))

# teste - scroll pra garantir que esteja visivel
driver.execute_script("arguments[0].scrollIntoView(true);", news_title)

# action de clique
news_title.click()
print("Notícia selecionada: ", news_title.text)
time.sleep(3)

# extraindo o texto 
content_p = driver.find_elements(By.CSS_SELECTOR, "p.content-text__container")
news_txt = "".join([p.text for p in content_p])

print("Texto extraído: ", news_txt[:500])  

# cria o prompt na openai pra ação de resumo
response = openai.Completion.create(
    model="text-davinci-003",  
    prompt=f"Resuma o seguinte texto em português:\n{news_txt}",
    max_tokens=150,
    temperature=0.7
)

resumo = response.choices[0].text.strip()
print("Resumo final: ")
print(resumo)

driver.quit()
