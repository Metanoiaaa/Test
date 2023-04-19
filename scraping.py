print("scraping")

import requests 

from bs4 import BeautifulSoup

pagina = requests.get("https://coinmarketcap.com")
# print(pagina.content)

heeldehtml = BeautifulSoup(pagina, 'html.parser')
tbody = heeldehtml.find('tbody')

print(tbody)

print(tbody.prettify)

coins = heeldehtml.find_all('tr')

for r,rij in coins:
  print(rij)