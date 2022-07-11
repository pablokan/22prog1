# El diccionario es una estructura de datos en formato clave: valor separados por coma. La clave habitualmente es una string y el valor es cualquier cosa

# diccionario tipo Registro
diccPersona = {
    "nombre": "Ana",
    "edad": 33,
    "hijos": ["Pedro", "Luisa", "Antonio"],
    "padres": {"madre": "Pepa", "padre": "Quico"},
}

for k, v in diccPersona.items():
    print(f"Clave: {k} --> Valor: {v}")

print(
    diccPersona["edad"]
)  # es parecido a la lista, solamente que en lugar de un índice tiene una string

listaPersona = [
    "Ana",
    33,
    ["Pedro", "Luisa", "Antonio"],
    {"madre": "Pepa", "padre": "Quico"},
]
print(listaPersona[1])
print("Nombre de los hijos:", listaPersona[2])
print("Nombre de los hijos:", diccPersona["hijos"])

# diccionario de tipo Homogéneo
d = {"perros": 2, "gatos": 3, "tortugas": 7}

