#!/usr/bin/env python
# coding: utf-8

# ## Gerador de logs

# In[14]:


import os
import datetime
import time
import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
import datetime


# In[ ]:





# In[40]:


# quando for criar o log, só precisar gerar um csv mesmo, sem os tempos, contento apenas o note da job + datetime.now(),
# para a partir de um outro arquivo que será o validador se a rotina gerou fazer o check se o arquivo do dia existe e se não
# aí sim gerar gerar notificação via email de que o arquivo n foi criado.


# In[10]:


inicio = datetime.datetime.now()


# In[18]:


fim = datetime.datetime.now()


# In[21]:


Tempo_total = fim - inicio


# In[22]:


print(Tempo_total)


# In[27]:


log = pd.DataFrame(np.array([[str(Tempo_total)[0:10], inicio.strftime("%b %d %Y %H:%M:%S"),fim.strftime("%b %d %Y %H:%M:%S") ]]),
columns=['Tempo total', 'Inicio', 'Fim'])
log.to_csv(r"C:\Users\Lucas\Desktop\log_rotina_1.csv", index=False, sep=';')


# In[35]:


a = datetime.datetime.now()
b = a.strftime("%b %d %Y").replace(" ", "_")


# In[36]:


print(b)


# In[39]:


log.to_csv(r"C:\Users\Lucas\Desktop\log_rotina_1_"+ b +".csv", index=False, sep=';')


# ## Aqui sim inicia o código validador, fazer em outro arquivo .py
# 

# In[2]:


import os.path


# In[10]:


nome_job = "A rotina_1 apresentou erro"
job_name = r"C:\Users\Lucas\Desktop\log_rotina_1_"


# In[11]:


data = datetime.datetime.now()
data_1 = data.strftime("%b %d %Y").replace(" ", "_")
print(data_1)


# In[7]:


nome_job_final = job_name+data_1+".csv" 
print(nome_job_final)


# In[15]:


if(os.path.exists(nome_job_final)):
    print('Rotina executada com sucesso')
else:
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "D:\Email"}  # Caminho do download da base
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--no-sandbox')
    chrome = webdriver.Chrome(r"C:\Users\Lucas\Desktop\chromedriver.exe", chrome_options=chrome_options)
    chrome.get("https://mail.google.com/mail/u/0/#inbox")
    chrome.maximize_window()
    
     # Entra no email
    #time.sleep(3)
    #chrome.find_element_by_id("identifierId").click()
    #chrome.find_element_by_id("identifierId").send_keys(credenciais["email"])
    #chrome.find_element_by_id("identifierId").send_keys(Keys.ENTER)
    #time.sleep(3)
    chrome.find_element_by_id("identifierId").send_keys("testeslucas820@gmail.com")
    chrome.find_element_by_id("identifierId").send_keys(Keys.ENTER)
    chrome.implicitly_wait(4)
    chrome.find_element_by_name("password").send_keys("Gatinha@10")
    chrome.find_element_by_name("password").send_keys(Keys.ENTER)
    #chrome.find_element_by_name("password").send_keys(Keys.ENTER)
    chrome.implicitly_wait(10)
    #ABAIXO ESTÁ BUSCANDO A PARTI DO FULL XPATH
    chrome.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div").click()
    
    chrome.implicitly_wait(6)
    chrome.find_element_by_name("to").send_keys("lucasdavihendry@gmail.com") # quem vai receber o email
    chrome.implicitly_wait(4)
    chrome.find_element_by_name("subjectbox").send_keys(nome_job) # Assunto
    chrome.implicitly_wait(4)
    
    chrome.find_element_by_xpath("//div[4]/table/tbody/tr/td/div/div[2]/div").click()
    
    time.sleep(5)
    chrome.close()

    
    
    #chrome.find_element_by_name("YPqjbf").send_keys("testeslucas820@gmail.com")
    #chrome.find_element_by_name("identifier").send_keys("testeslucas820@gmail.com")
    #chrome.find_element_by_name("ctl00$ContentPlaceHolder1$PasswordTextBox").send_keys(credenciais["Gatinha@10"])
    #chrome.find_element_by_name("ctl00$ContentPlaceHolder1$SubmitButton").click()
    #time.sleep(4)


# In[ ]:




