def main():
    people = [
        "Vikki Tewkesbury,France,30-01-2000",
        "Virgie Brach,France,04-02-1994",
        "Adeline La Padula,France,18-06-2002",
        "Willy Branscombe,Argentina,21-11-1997",
        "Diane Piffe,France,07-08-1993",
        "Britta Causbey,France,24-04-1991",
        "Elisabeth Cleeve,France,04-03-1991",
        "Rafael Ivanchenkov,France,28-04-2002",
        "Zerk Milsom,Norway,03-12-1994",
        "Adorne Ovington,United States,17-08-1991",
        "Kathryn Backshell,United States,04-03-1992",
        "Blake Colbeck,United States,18-01-1999",
        "Arron Bresnahan,United States,03-07-2001",
        "Deloria Dominguez,France,31-07-1990",
        "Grenville Aldersea,Argentina,11-01-2001",
        "Jemimah Haughian,Argentina,30-11-1998",
        "Con Gethen,United States,06-06-1992",
        "Roxie Igoe,France,31-03-2002",
        "Hollyanne Mottley,United States,05-01-1996",
        "Ambrosio Cadore,Norway,09-12-2002"
    ]
    people = [people[i].split(",") for i in range(len(people))]
    countries = ['Germany', 'United States', 'Norway', 'France']
    solve_1(people, countries)
    solve_2(people)

def solve_1(people, countries):
    cont_arg = 0
    for i in range(len(people)):
        if people[i][1] == "Argentina":
            cont_arg += 1
    print(f"La cantidad de personas de Argentina es {cont_arg}\n")

    print(f"Opciones:{countries}")
    country = input_country(countries,"Ingrese otro país además de Argentina: ")
    cont_country = 0
    for i in range(len(people)):
        if people[i][1] == country:
            cont_country += 1
    print(f"La cantidad de personas de Norway es: {cont_country}\n")

def solve_2(people):
    initial = input_letter("Ingrese inicial de apellido: ")
    print(f"Las fechas de nacimiento de las personas cuyo apellido empieza con {initial} son:")
    for i in range(len(people)):
        aux = people[i][0].find(" ")
        if people[i][0][aux + 1] == initial: 
            print(people[i][2])


def input_country(countries, text=""):
    while True:
        try:
            country = input(text)
            if country in countries:
                break
            else:
                raise Exception()
        except:
            print("Opción inválida")
    return country

def input_letter(text=""):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Odio la ñ :)
    while True:
        try:
            letter = input(text).upper()
            if letter in letters:
                break
            else:
                raise Exception()
        except:
            print("Entrada inválida")
    return letter

if __name__ == "__main__":
    main()