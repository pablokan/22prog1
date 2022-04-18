# Pasar un período expresado en segundos a un período
# expresado en días, horas, minutos y segundos.

totalSegundos = 1_000_000  # notación lower camel case
# total_segundos ---> notación snake case
# totalSegundos = int(input("Ingrese el monto de segundos: "))

dias = totalSegundos // 86400
resto = totalSegundos - (dias * 86400)
horas = resto // 3600
resto = resto - (horas * 3600)
minutos = resto // 60
segundos = resto - (minutos * 60)

print(
    "El monto total de segundos",
    totalSegundos,
    "es equivalente a",
    dias,
    "dias,",
    horas,
    "horas,",
    minutos,
    "minutos y",
    segundos,
    "segundos.",
)
