p = {"nombre": "Juan", 
"nombresHijos": ["Pedro", "Ana", "José"], "nombresPadres": {"Padre": "Juan", "Madre": "Maria"}
}

print(p["nombresHijos"])
for hijo in p["nombresHijos"]:
    print(hijo)

humane = p["nombre"]
madre = p["nombresPadres"]["Madre"]
print(f"La madre de {humane} se llama {madre}")
