import os
from flask import Flask, request

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return ""


resp = requests.get('https://ge.globo.com/futebol/copa-do-mundo/2022/')

cont = resp.content

site = BeautifulSoup(cont, 'html.parser')

tab = site.find('div', attrs={'class':'ranking-content'})

axies= tab.find_all('div', attrs={'class':'jogador-nome'})

axies_lista = [i.text for i in axies]

print(axies_lista)

if __name__ =="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
    
