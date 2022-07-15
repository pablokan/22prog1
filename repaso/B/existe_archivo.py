import os
from datetime import date
hoy = date.today()
print(hoy.month)
nombreArchivo = str(hoy.month) + ".txt"
print(nombreArchivo)

if os.path.exists('repaso/B/personas.txt'):
    print("existe!!!")

