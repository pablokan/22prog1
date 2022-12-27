def edad(fechaNac):
    from datetime import date
    # usar date para validar fecha de entrada
    dN, mN, aN = [int(x) for x in fechaNac.split('/')]
    try:
        date(aN, mN, dN)
    except:
        return 'Fecha inexistente'
    hoy = date.today()
    e = hoy.year - aN
    if (mN > hoy.month) or (mN == hoy.month and dN > hoy.day):
        e -= 1
    return e

print(edad('3/6/1965')) # Devuelve: 57
print(edad('3/12/2000')) # Devuelve: 21
print(edad('30/11/1992')) # Devuelve: 29
print(edad('29/2/2007')) # Devuelve: 'Fecha inexistente'

