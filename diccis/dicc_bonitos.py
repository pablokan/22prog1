d = {"nombre": "Juan", "nombresHijos": ["Pedro", "Ana", "José"], "nombresPadres": {"Padre": "Juan", "Madre": "Maria"}}

print("El nombre de la madre es", d["nombresPadres"]["Madre"])

for hijo in d["nombresHijos"]:
    print(hijo)
    



