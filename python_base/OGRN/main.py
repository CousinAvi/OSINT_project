import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import json
import sys

class Econom_org():
    def __init__(self,info):
        self.info = info
    def main(self):
        response = requests.get('https://zachestnyibiznes.ru/search?query=%s'%self.info)
        soup = BeautifulSoup(response.text, 'lxml')
        headers = {}
        rows = soup.find_all("tr")
        thead = soup.find("thead").find_all("th")
        for i in range(len(thead)):
            headers[i] = thead[i].text.strip().lower()

        def func_parse(cells,headers):
            item = {}
            heads = ['название','статус','инн','руководитель','регистрация','адрес','Посмотреть']
            for index in headers:
                try:
                    if heads[index] == 'адрес':
                        item[heads[index]] = cells[index].text.replace("\nПо данным портала ЗАЧЕСТНЫЙБИЗНЕС\n",'')
                    else:
                        item[heads[index]] = cells[index].text
                except:
                    pass
            return item

        mould = []
        for row in rows:
            cells = row.find_all("td")
            a = func_parse(cells,headers)
            mould.append(a)
        return mould
