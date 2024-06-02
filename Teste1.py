from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Configura as opções do Chrome para ignorar os erros de certificado SSL
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Inicializa o driver do Chrome com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

# Abre a página da web
driver.get("https://pb.ongame.net/ranking/individual/semanal/")

# Espera até que o botão para aceitar os termos seja clicável (se necessário)
try:
    termos = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[2]/div/button")))
    termos.click()
except:
    print("Botão para aceitar os termos não encontrado ou não clicável.")

# Espera até que a tabela seja carregada
try:
    tabela_carregada = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/section/div/table')
except:
    print("Tabela não carregada.")

# Encontra todos os elementos <tr> que representam cada linha da tabela
linhas = tabela_carregada.find_elements(By.TAG_NAME, 'tr')

dados_tabela = []

# Itere sobre as primeiras 10 linhas (começando da segunda linha se houver cabeçalho)
for i in range(1, min(len(linhas), 11)):
    colunas = linhas[i].find_elements(By.TAG_NAME, 'td')  # Pegue todas as células da linha

    # Extrai os dados da linha
    rank = colunas[0].text
    patente = colunas[1].find_element(By.TAG_NAME, "img").get_attribute("title")
    nick = colunas[2].text
    exp = colunas[3].text
    kd = colunas[4].text
    hs = colunas[5].text
    win = colunas[6].text
    
    # Imprime os dados
    print("Rank:", rank)
    print("Patente:", patente)
    print("Nickname:", nick)
    print("exp:", exp)
    print("kd:", kd)
    print("HS: ", hs)
    print("WIN: ", win)
    print("\n")

# Armazene os dados em um dicionário
    dados_linha = {
        "rank": rank,
        "patente": patente,
        "nickname": nick,
        "exp": exp,
        "kd": kd,
        "hs": hs,
        "win": win
    }
    
    # Adicione o dicionário à lista
    dados_tabela.append(dados_linha)    

#Fecha o navegador
driver.quit()

# Escreva os dados em um arquivo JSON
with open('dados_tabela.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados_tabela, json_file, ensure_ascii=False, indent=4)