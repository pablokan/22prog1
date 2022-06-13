# 1) El total adeudado en el año 2021
# 2) La cantidad de mujeres que tengo en el listado
# 3) El nombre y la dirección de correo del varón que más debe

deudores = [
    "1,Veriee,vvasilkov0@qq.com,Female,$374324.12,09/04/2022,Besançon",
    "2,Lizbeth,locklin1@tiny.cc,Female,$423222.26,14/09/2021,Jawand",
    "3,Tymon,thillum2@diigo.com,Male,$591323.65,08/01/2022,Rîbniţa",
    "4,Teddie,tschofield3@ehow.com,Male,$279894.15,12/05/2022,Tlogoagung",
    "5,Dom,dantonin4@squarespace.com,Male,$884488.11,04/03/2022,Tonjongsari",
    "6,Armstrong,acreegan5@reverbnation.com,Male,$136930.77,07/08/2022,Xianning",
    "7,Micky,mmaccall6@elpais.com,Female,$925498.10,16/08/2021,Dongping",
    "8,Mickie,mprosser7@alexa.com,Male,$634854.83,22/05/2022,Perm",
    "9,Nadya,ngerrett8@over-blog.com,Female,$682885.94,26/04/2022,Champaign",
    '10,Donni,dboots9@digg.com,Female,$748880.01,02/04/2022,Normanton',
    "11,Dalli,dmorecombea@wordpress.com,Male,$490253.97,26/02/2022,Serra",
    '12,Fionna,fshanksterb@mashable.com,Female,$953863.00,29/01/2022,Ccuntuma',
    "13,Melesa,mmacinnesc@si.edu,Female,$473316.46,21/07/2022,Shihua",
    '14,Orelle,oshobbrookd@t.co,Female,$193841.90,21/11/2021,Huangtan',
    '15,Gayelord,ghasloche@gmpg.org,Male,$325836.11,20/06/2022,Sehwān',
    '16,Florencia,fforstf@addthis.com,Female,$632385.67,17/05/2022,Buenavista',
    '17,Pam,pbelfeltg@lulu.com,Female,$137358.07,30/11/2021,Maclear',
    '18,Ollie,okubalekh@feedburner.com,Female,$196640.52,20/05/2022,Kebon',
    '19,Wyn,wlingeri@dropbox.com,Male,$558827.34,10/05/2022,Gimry',
    '20,Vachel,vburbankj@topsy.com,Male,$140948.04,25/06/2022,Bungoma'
    ]


max=0                               # se inicializa el máximo en 0
nombre=''                           # se guardará el nombre del máximo deudor
correo=''                           # se guardará el correo del máximo deudor
cantMujeres=0                       # se inicializa la cantidad de mujeres en 0
deuda2021=0
for elemento in deudores:           # Para todos los elementos de la lista deudores
    dato=elemento.split(',')        #       Se obtiene una lista con los elementos del deudor separados por ","
    fecha=dato[5].split('/')        #       Se obtiene una lista con la fecha correspondiende a la deuda, y sus elementos son los separados por "/"
    anio=fecha[2]                   #       Se obtiene el año de la fecha anterior
    if anio=='2021':                #       Si anio es 2021, se guarda el deudor en la lista de 2021
        deuda=dato[4]               #           Se obtiene la deuda
        deuda=float(deuda[1:])      #           Se obtiene el valor numérico de la deuda
        deuda2021+=deuda            #           Se suma la deuda a la deuda de 2021
               
    if dato[3]=='Male':             #       Si el género del deudor (dato[3]) es "Male"
        deuda=dato[4]               #           Se obtiene la deuda de ese deudor
        deuda=float(deuda[1:])      #           Se obtiene el valor numérico de la deuda
        if deuda>max:               #           Si la deuda es mayor al valor guardado en "max" entonces 
            max=deuda               #               esta deuda es el nuevo máximo
            nombre=dato[1]          #               Se guarda el nombre del máximo deudor
            correo=dato[2]          #               Se guarda el corredo del máximo deudor

    if dato[3]=='Female':           #       Si el género del deudor (dato[3]) es "Female"
        cantMujeres+=1              #           Se aumenta en 1 la candidad de mujeres
                                     

print('1) La deuda total de 2021 es: $'+(str(round(deuda2021,2))))
print('2) La cantidad total de mujeres es:',cantMujeres)
print('3) El varón que más debe es:',nombre,'y su correo es',correo)


