from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)

li2 = [2, 1, 3]
li2.sort()
print(li2)

li1 = [2, 1, 3]
dicc = {2: 'D', 1: 'C', 5: 'B', 4: 'E', 3: 'A'}
print(sorted(dicc))
print(sorted(dicc.values()))
print(sorted(dicc.items()))

print(sorted("It's a test string from Andrew".split()))
print(sorted("It's a test string from Andrew".split(), key=str.lower))

usuarios = [
    {'nombre': 'Pablo', 'apellido': 'Kan'},
    {'nombre': 'Juan', 'apellido': 'Kan'},
    {'nombre': 'Lidia', 'apellido': 'Zeitz'},
    {'nombre': 'Miranda', 'apellido': 'Kan'},
    {'nombre': 'Quico', 'apellido': 'Denmark'},
    {'nombre': 'Amancia', 'apellido': 'Lantos'}
]

print(sorted(usuarios, key=lambda user: user['nombre'])) 
print(sorted(usuarios, key=lambda user: user['apellido'])) 
pp.pprint(sorted(usuarios, key=lambda user: (user['apellido'], user['nombre'])))

L = ["cccc", "b", "dd", "aaa"]
print ("Normal sort :", sorted(L))
print ("Sort with len :", sorted(L, key = len))



