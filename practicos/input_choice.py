def inputChoice(msg, choices):
    valid = False
    while not valid:
        print("Opciones:", choices)
        choice = input(msg).upper()
        if choice in choices:
            valid = True
        else:
            print("Opción inválida")
            print()
    return choice

if __name__ == "__main__":
    a = inputChoice("Ingrese opción: ", ["SI", "NO"])
    print(a)
