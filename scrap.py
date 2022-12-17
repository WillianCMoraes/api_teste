from bs4 import BeautifulSoup
import requests

import os
from flask import Flask, request


resp = requests.get('https://ge.globo.com/futebol/copa-do-mundo/2022/')

cont = resp.content

site = BeautifulSoup(cont, 'html.parser')

tab = site.find('div', attrs={'class':'ranking-content'})

axies= tab.find_all('div', attrs={'class':'jogador-nome'})

axies_lista = [i.text for i in axies]

print(axies_lista)


if __name__ =="__main__":
    port = int(os.environ.get("PORT", 5000))
  