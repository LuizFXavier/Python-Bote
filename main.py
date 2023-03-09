from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import string

options = Options()
options.add_experimental_option("detach", True)
delay = 3

nav = webdriver.Edge(options=options)
nav.get("https:/www.bing.com/")
sleep(6)

# select 2 digits at random
digitos = random.choices(string.digits, k=2)

# select 9 uppercase letters at random
letras = random.choices(string.ascii_uppercase, k=9)

# shuffle both letters + digits
sample = random.sample(digitos + letras, 11)

result = ''.join(sample)

search = nav.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div[2]/form/div[1]/div/textarea")

search.send_keys(result,Keys.ENTER)

try:
    cookieYes = WebDriverWait(nav, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/button")))
    
    cookieYes.click()    
except:
    pass

sleep(2)

for i in range(30):
    
    try:
        print("lolololololololololololololol")
        search2 = WebDriverWait(nav, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/form/div/textarea")))
           
        digitos = random.choices(string.digits, k=2)

        letras = random.choices(string.ascii_uppercase, k=9)

        sample = random.sample(digitos + letras, 11)

        delete = webdriver.Keys.BACKSPACE * 11

        result = ''.join(sample)

        search2.send_keys(delete,result,Keys.ENTER)
        
    except:
        pass