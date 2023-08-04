#Librerias 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time
import pandas as pd

#Lib sistema
import os
import sys

#Variables sistema
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])




#Config Navegador
driver = webdriver.Firefox(
    executable_path=r'C:\Users\Camilo García\Desktop\RPA\geckodriver.exe')

#Variables globales
url="https://es.wikipedia.org/wiki/Anexo:Ganadores_del_Premio_Nobel"
final_path = os.path.join(path, "Final_Path")


# Inicializar Navegador
driver.maximize_window()
time.sleep(1)


driver.get(url)


df = {'Año':[], 'Fisica':[], 'Quimica':[], 'Medicina':[], 'Literatura':[], 'Paz':[], 'Economia': []}


for i in range (1,83):
    año_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[1]')))
    año_nobel_text = año_nobel.text
    df['Año'].append(año_nobel_text)

    fisica_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[2]')))
    fisica_nobel_text = fisica_nobel.text
    df['Fisica'].append(fisica_nobel_text)

    quimica_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[3]')))
    quimica_nobel_text = quimica_nobel.text
    df['Quimica'].append(quimica_nobel_text)

    medicina_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[4]')))
    medicina_nobel_text = medicina_nobel.text
    df['Medicina'].append(medicina_nobel_text)

    literatura_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[5]')))
    literatura_nobel_text = literatura_nobel.text
    df['Literatura'].append(literatura_nobel_text)

    paz_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[6]')))
    paz_nobel_text = paz_nobel.text
    df['Paz'].append(paz_nobel_text)

    economia_nobel = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                    f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[7]')))
    economia_nobel_text = economia_nobel.text
    df['Economia'].append(economia_nobel_text)

df = pd.DataFrame(df)
print(df)
df.to_csv(final_path + "\\extraccionNobels.csv", sep=";", index=False)






