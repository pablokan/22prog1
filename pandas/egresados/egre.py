#import pandas as pd
# d = pd.read_csv('historico_itec.csv')
# print(d)

import csv
from pprint import pprint
with open('historico_itec.csv', 'r') as file:
    reader = csv.reader(file)
    lista = [(row[10][-4:], row[11]) for row in reader]

pprint(lista)


c = 0
for e in lista:
    if e[0] == '2015' and e[1].startswith('A'):
        c += 1
print(c)

