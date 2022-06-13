# Tengo un archivo de deudores. Quiero obtener:
# El total adeudado en el año 2021
# La cantidad de mujeres que tengo en el listado
# El nombre y la dirección de correo del varón que más debe

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
deudor = []
email = []
Sexo = []
cont = 0
direccion= []
anio = []
deuda = []

for i in range (len(deudores)):
    PosComa = deudores[i].find(",")
    PosComa2 = deudores[i][PosComa+1:].find(",")
    PosComa3 = deudores[i][PosComa+1+PosComa2+1:].find(",")
    Nombre = deudores[i][PosComa+1:PosComa+1+PosComa2]
    deudor.append(Nombre)
    Posemail = deudores[i][PosComa+1+PosComa2:PosComa+1+PosComa2+1+PosComa3]
    email.append(Posemail)
    posSexo = deudores[i][PosComa+1+PosComa2+1+PosComa3+1:].find(",")
    sexo = deudores[i][PosComa+1+PosComa2+1+PosComa3+1:PosComa+1+PosComa2+1+PosComa3+1+posSexo]
    Sexo.append(sexo)
    monto = deudores[i][PosComa+1+PosComa2+1+PosComa3+1+posSexo+1:].find(",")
    debe = deudores[i][PosComa+1+PosComa2+1+PosComa3+1+posSexo+1:PosComa+1+PosComa2+1+PosComa3+1+posSexo+1+monto]
    deuda.append(debe)
    plata = deuda[i][1:]
    dir = deudores[i][::-1].find(",")
    direccionD = deudores[i][-dir:]
    direccion.append(direccionD)
    posfecha = deudores[i][-(dir+11):-(dir+1)]
    anio.append(posfecha)
    
    if Sexo[i] == "Female":
        cont +=1
print(Sexo)
    

print("la cantidad de mujeres son: ", cont)
