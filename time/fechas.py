# Localización de fechas en Español 
import locale
loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, loc)

from datetime import datetime, timedelta, date

ahora = datetime.now() # Fecha y hora actual

# Cálculo de edad
""" ahora = date.today() # Fecha actual solamente, o sea, sin la hora
fechaCumple = date(1965, 6, 28)
print((ahora - fechaCumple) // timedelta(days=365.2425))
 """

""" 
# Operaciones con fechas
quinceDias = ahora + timedelta(days=15)
print(ahora.isoformat())
print(quinceDias.isoformat())
print(quinceDias.strftime("%A %d de %B del %Y - %H:%M horas"))
 """

print(ahora.strftime("%d/%m/%Y"))
#print(ahora.strftime("%a %d %B %Y %I:%M"))
#print(ahora.strftime("%A %d de %B del %Y - %H:%M horas"))
#print(ahora.strftime('Número de día en el año: %j'))
#print(ahora.strftime('Número de semana en el año: %U'))
#print(quinceDias.strftime("%A %d de %B del %Y - %H:%M horas"))
#print(ahora.strftime("%A"))
#print(ahora.strftime("%a"))

#print(ahora.month)
""" 
hoy = date.today()
for d in range(7):
    dia = hoy - timedelta(days=d)
    print(dia, dia.strftime("%A"))
 """
""" 
%a Locale's abbreviated weekday name.
%A Locale's full weekday name.    
%b Locale's abbreviated month name.  
%B Locale's full month name.
%c Locale's appropriate date and time representation.    
%d Day of the month as a decimal number [01,31].
%H Hour (24-hour clock) as a decimal number [00,23].
%I Hour (12-hour clock) as a decimal number [01,12].        
%j Day of the year as a decimal number [001,366].
%m Month as a decimal number [01,12].
%M Minute as a decimal number [00,59].  
%p Locale's equivalent of either AM or PM.  
%S Second as a decimal number [00,61].
%U Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w Weekday as a decimal number [0(Sunday),6].        
%W Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x Locale's appropriate date representation.    
%X Locale's appropriate time representation.      
%y Year without century as a decimal number [00,99].    
%Y Year with century as a decimal number.
%Z Time zone name (no characters if no time zone exists).  
%% A literal "%" character
"""