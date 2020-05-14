from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd
import requests
from bs4 import BeautifulSoup as bp

import time

chrome_path = r'C:\Users\caiom\Documents\Teste\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)

driver.get('https://www.investsite.com.br/balanco_patrimonial_passivo.php?cod_negociacao=ITSA3')
time.sleep(2)

#anos = ["2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
anos = ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
#anos = ["2009","2010","2011","2012"]
tri = ["1231","0930","0630","0331"]

for i in anos:
    select = Select(driver.find_element_by_id("ano_dem"))
    select.select_by_value(i)
    time.sleep(12)
    for j in tri:
        select1 = Select(driver.find_element_by_id("mes_dia_dem"))
        select1.select_by_value(j)
        time.sleep(12)
        soup=bp(driver.page_source, 'lxml')
        table = soup.findAll(name='table')
        table_str = str(table)
        df = pd.read_html(table_str)[1]
        df.to_excel(r'D:\\ProjectsPython\\Empresas\\ItauSA\\Selenium\\Passivo\\Passivo_'+i+'_'+j+'.xlsx', header=True, sheet_name='Passivo_'+i+'_'+j)
driver.quit()
