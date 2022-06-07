fechas = [
    "01-01-2021",
    "02-02-2019",
    "23-11-1989"
]

personas = [
"José,12",
"Ana,33",
"Quico,88"
]
""" 
print("Días que figuran en las fechas de la lista:")
for i in range(len(fechas)):
    fecha = fechas[i]
    print(fecha[:2])


for i in range(len(personas)):
    persona = personas[i]
    print(persona)

"""

s1 = "hola como te va"
l1 = s1.split(" ")
print(l1)
l2 = s1.split("o") # ["h", "la c", "m", " te va"]
print(l2)

s2 = "22x53x48x90"
l2 = s2.split("x") # ['22', '53', '48', '90']
print(l2)
