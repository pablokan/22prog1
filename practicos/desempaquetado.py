def saludo(n, e):
    print(f"Hola {n}, tenés {e} años")

saludo("José", 44)

persona = ["Ana", 55]
saludo(persona[0], persona[1])
saludo(*persona) # unpack