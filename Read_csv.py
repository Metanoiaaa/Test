print("Start csv read applicatie")

import pandas

df = pandas.read_csv("pokemon.csv")

print(df["Name"])

for rij in df.iterrows():
    print(rij)
    