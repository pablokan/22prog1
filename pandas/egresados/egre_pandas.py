import pandas as pd
import csv
from pprint import pprint

with open('historico_itec.csv', 'r') as file:
    reader = csv.reader(file)
    lista = [(row[10][-4:], row[11]) for row in reader if row[10] != '']
lista.pop(0)
lista = [(int(t[0]), t[1]) for t in lista if int(t[0])>=2015]

df = pd.DataFrame.from_records(lista, columns=["Egreso", "Carrera"])
print(pd.crosstab(df.Carrera, df.Egreso))


# dfSize = df.groupby(['Egreso', 'Carrera']).size()
#print(df.value_counts(["Egreso", "Carrera"]))



