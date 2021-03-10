import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://zachestnyibiznes.ru/search?query=Сбербанк')
html = response.text
#soup = BeautifulSoup(html, 'lxml')
#table = soup.find("div",{"class":""})
#print(table)