from main import IAMain
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install()) 

options.add_argument("start-maximized")

# desativa uma variedade de recursos no mecanismo Blink relacionados à automação.
# faz com que o google não bloqueie o acesso ao login
options.add_argument("--disable-blink-features=AutomationControlled")


nav = webdriver.Chrome(options=options,service=service)
nav.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ASKXGp2nshLuqF-You3g9kXc7dscl1j20q92sgaPsFeD6IDZaHVvV3JT_0EpIC2bGbfhRl83oEpjnA&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1812953031%3A1705497790545188&theme=glif#inbox")

nav.find_element(By.ID,'identifierId').send_keys('YOUR EMAIL')

time.sleep(1)

nav.find_element(By.ID,'identifierNext').click()

time.sleep(5)

nav.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('YOUR PASSWORD')

time.sleep(1)

nav.find_element(By.ID,'passwordNext').click()

time.sleep(10)
i = 1

from main import mainIA

#voce pode modificar para o looping acontecer quantas vezes você desejar, até infinitamente:
for x in range(10):
    nav.find_element("xpath", f'/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[2]/div/table/tbody/tr[{i}]').click()
    time.sleep(2)
    email_i = nav.find_element('xpath','/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]').text
    print(email_i)

    #executa a função criada no outro arquivo com o email que verificaremos
    respostaIA = IAMain(email_i)

    if respostaIA == 1:
        #caso a IA reconheça como spam, manda o email para a lixeira
        time.sleep(2)
        nav.find_element('xpath','//*[@id=":4"]/div[2]/div[1]/div/div[2]/div[3]/div').click()
        
        
    elif respostaIA == 0:
        time.sleep(2)
        #caso a IA NÃO reconheça como spam, apenas volta para a pagina inicial a repete o processo na linha seguinte
        nav.find_element('xpath','//*[@id="gb"]/div[2]/div[1]/div[4]/div/a/img').click()
        i += 1

