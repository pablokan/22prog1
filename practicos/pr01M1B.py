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

t = 0
for x in range(len(deudores)):
    deudor = deudores[x]
    print(deudor)
    if "/2021" in deudor:
        deudor = deudor.split(",")
        print(deudor)
        print(deudor[4])
        plata = deudor[4]
        print(plata[1:])
        t += float(deudor[4][1:])
print("Total deuda año 2021:", round(t,2))

w = 0
for x in range(len(deudores)):
    deudor = deudores[x]
    if "/2021" in deudor:
        posPeso = deudor.find("$")
        deudor = deudor[posPeso+1:]
        posComa = deudor.find(",")
        w += float(deudor[:posComa])
print("Total deuda año 2021:", round(w,2))

c = 0
for x in range(len(deudores)):
    if "Female" in deudores[x]:
        c += 1
print("La cantidad de mujeres deudoras es", c)

mayorDeuda = 0
for x in range(len(deudores)):
    deudor = deudores[x]
    if "Male" in deudor:
        deudor = deudor.split(",")
        deuda = float(deudor[4][1:])
        if deuda > mayorDeuda:
            mayorDeuda = deuda
            mayorDeudor = deudor[1]
            mail = deudor[2]
print("El mayor deudor es", mayorDeudor, mail)



    




