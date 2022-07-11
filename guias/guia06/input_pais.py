def inputPais(msg, paises):
    valid = False
    while not valid:
        print(paises)
        p = input(msg).upper()
        if p in paises:
            valid = True
        else:
            print("Ese país no está en el listado")
        print()
    return p

if __name__ == "__main__":
    q = inputPais("Ingrese algun pais: ", ["KENIA", "SUDÁN"])
    print(f"Ingresó {q}")

