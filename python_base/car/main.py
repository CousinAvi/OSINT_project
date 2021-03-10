import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import json
import sys
from googlesearch import search
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class CarSearch():
    def __init__(self,nomer):
        self.nomer = nomer
    def pars(self,index,soup):
        links = [ link for link in soup.findAll('div', {'class': 'ng-list ng-list_theme_extended-info-card'})[index] ]
        #print(links)
        stroka = links[1]

        soup2 = BeautifulSoup(str(stroka), 'lxml')
        mould = [link.get('href') for link in soup2.findAll('a', {'class': 'ng-item'})]
        return mould[0]

    def get_photo(self,link):
        mould = []
        response = requests.get(link)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        images = soup.findAll('img')
        for image in images:
            #print image source
            mould.append({'img':image['src']})
            #print (image['src'])
        mould = [part for part in mould if part['img'].find('https') != -1]
        linki_drom = [link.text.strip() for link in soup.findAll('div', {'class': 'ng-text_gray ng-text_small ng-photo__origin'})]
        #print(linki_drom)
        return linki_drom

    def main(self):
        #opts = Options()
        #opts.headless = True
        #assert opts.headless  # без графического интерфейса.

        browser = webdriver.Remote(
           command_executor='http://127.0.0.1:9515',
           desired_capabilities=DesiredCapabilities.CHROME)
        browser.get('https://www.nomerogram.ru')
        elem = browser.find_element_by_name("series1")
        elem.send_keys("%s"%self.nomer[0])
        elem = browser.find_element_by_name("number")
        elem.send_keys("%s"%self.nomer[1:4])
        elem = browser.find_element_by_name("series2")
        elem.send_keys("%s"%self.nomer[4:6])
        elem = browser.find_element_by_name("region")
        elem.send_keys("%s"%self.nomer[6:9])

        new = browser.find_element_by_class_name("ng-button_load-cont")
        new.click()
        try:
            delay = 2
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'ng-card')))
        except:
            browser.close()
            browser.quit()
            return []

        soup = BeautifulSoup(browser.page_source, 'lxml')


        mould = []
        try:
            mould_card = [link.get('href') for link in soup.findAll('div', {'class': 'ng-card'})]
            chislo_card = (len(mould_card))
            vyvod = []
            for index in range(chislo_card):
                vyvod.append(self.pars(index,soup))
            for part in vyvod:
                otvet = self.get_photo(part)
                if otvet == []:
                    mould.append({'link': part,
                                  'info' : 'Ссылка на фото'})
                else:
                    mould.append({'link': otvet[0].replace('Источник: ',''),
                                  'info' : 'Ссылка на Дром'})
        except:
            browser.close()
            browser.quit()
            return []
        browser.close()
        browser.quit()
        return mould
