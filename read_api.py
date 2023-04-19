print("api read applicatie")

import requests

paginaresultaat = requests.get("https://catfact.ninja/facts")
print(paginaresultaat)

feitjes= paginaresultaat.json()

print(feitjes["current_page"])
print(feitjes["data"] [0])
print(feitjes["data"] [0] ["fact"])

