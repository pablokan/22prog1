persona1 = {
    "nombre": "Ana",
    "edad": 33,
    "hijos": ["Pedro", "Luisa", "Antonio"],
    "padres": {"madre": "Pepa", "padre": "Quico"},
}

persona2 = {
    "nombre": "Luisa",
    "edad": 21,
    "hijos": [],
    "padres": {"madre": "Pepa", "padre": "Quico"},
}


def obtieneEdad(d):
    return d["edad"]

print(obtieneEdad(persona1))
print(obtieneEdad(persona2))

listaPersonas =[
    {
        "nombre": "Juan",
        "edad": 56, 
        "nombresHijos": ["Pedro", "Ana", "José"], 
        "nombresPadres": {"Padre": "Juan", "Madre": "Maria"}
    },
    {
        "nombre": "Luisa",
        "edad": 87, 
        "nombresHijos": ["Quico", "Pepita"], 
        "nombresPadres": {"Padre": "Octavio", "Madre": "Sonia"}
    },
    {
        "nombre": "Ernesto",
        "edad": 22, 
        "nombresHijos": ["Victoria"], 
        "nombresPadres": {"Padre": None, "Madre": "Katia"}
    }
]

# recorro la lista de Personas (cada una es un diccionario) y les aplico la función que obtiene la edad
for persona in listaPersonas:
    print("Edad:", obtieneEdad(persona))
