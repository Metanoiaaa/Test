print("scraping")

import requests 

from bs4 import BeautifulSoup

pagina = requests.get("https://coinmarketcap.com")
# print(pagina.content)

heeldehtml = BeautifulSoup(pagina, 'html.parser')
tbody = heeldehtml.find('tbody') #naam van element zoek bepaald element


print(tbody)

print(tbody.prettify)

#coins = heeldehtml.find('class= "naam van class"')

for r,rij in coins:
  print(rij)

print("tweede commit")
jajajas