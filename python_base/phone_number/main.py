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
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import pandas as pd
import os

def Twitter():
    browser.get('https://twitter.com/account/begin_password_reset')
    search_form = browser.find_element_by_name('account_identifier')
    search_form.send_keys('%s'%self.number)
    #wait = ui.WebDriverWait(browser,30)
    #button = browser.find_element_by_class_name('Form')
    search_form.submit()
    #button.click()

    #wait.until(lambda browser: browser.find_element_by_class_name("clearfix uiHeaderTop"))
    delay = 2 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-inline')))
        #print("Twitter +")
        Twitter = '+'

    except:
        Twitter = '-'
        #print ("Twitter -")

class Phone_Number():

    def __init__(self,number):
        self.number = number


    def main(self):        
        directory = 'python_base/phone_number/info'
        files = os.listdir(directory)
        code = self.number[2:5]
        
        number = self.number[5:]
        flag = True
        if code[0] == '3':
            file_take = files[0]
        elif code[0] == '4':
            file_take = files[1]
        elif code[0] == '8':
            file_take = files[2]
        elif code[0] == '9':
            file_take = files[3]
        else:
            flag = False
            operator = "Нет данных"
            region = "Нет данных"
        code = int(code)
        number = int(number)
        if flag:
            directory = directory+'/'+file_take
            df = pd.read_csv(directory, sep=';', comment='#')
            search = df.columns[0]
            from_index = df.columns[1]
            to_index = df.columns[2]
            temp = df.loc[df[search] == code]
            temp2 = temp.loc[temp[from_index] <= number]
            temp3 = temp2.loc[temp2[to_index] >= number]
            operator = temp3.values[0][4]
            region = temp3.values[0][5]

        response = requests.get('https://api.whatsapp.com/send?phone=%s'%self.number)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        mould = [part.text for part in soup.findAll('a', {'class': '_36or _2y_c _2z0c _2z07'})]
        if mould[0] == 'Перейти в чат':
            Whats = '+'
        else:
            Whats = '-'

        opts = Options()
        opts.headless = True
        assert opts.headless  # без графического интерфейса.
        #firefox_profile = webdriver.FirefoxProfile()
        #firefox_profile.set_preference('permissions.default.stylesheet', 2)
        #firefox_profile.set_preference('permissions.default.image', 2)
        #firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        browser = webdriver.Remote(
            command_executor='http://127.0.0.1:9515',
            desired_capabilities=DesiredCapabilities.CHROME,
            options = opts)

        browser.get('https://www.facebook.com/login/identify/?ctx=recover')
        search_form = browser.find_element_by_id('identify_email')
        search_form.send_keys('%s'%self.number)
        button = browser.find_element_by_name('did_submit')
        button.click()
        delay = 2 # seconds
        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'initiate_interstitial')))
            if (browser.current_url) != 'https://www.facebook.com/login/identify/?ctx=recover':
                Facebook = '+'

        except:
            Facebook = '-'

        VK = '-'
        
        OK = '+'
        browser.quit()
        return (operator,region,Whats,VK,OK,Facebook)
