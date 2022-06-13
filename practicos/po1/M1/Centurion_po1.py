deudores = [
    "1,Veriee,vvasilkov0@qq.com,Female,$374324.12,09/04/2022,Besançon",
    "2,Lizbeth,locklin1@tiny.cc,Female,$423222.26,14/09/2021,Jawand",
    "3,Tymon,thillum2@diigo.com,Male,$591323.65,08/01/2022,Rîbniţa",
    "4,Teddie,tschofield3@ehow.com,Male,$279894.15,12/05/2022,Tlogoagung",
    "5,Dom,dantonin4@squarespace.com,Male,$884488.11,04/03/2022,Tonjongsari",
    "6,Armstrong,acreegan5@reverbnation.com,Male,$136930.77,07/08/2022,Xianning",
    "7,Micky,mmaccall6@elpais.com,Female,$925498.10,16/08/2021,Dongping",
    "8,Mickie,mprosser7@alexa.com,Male,$634854.83,22/05/2022,Perm"
    ]

#1)
valores=[]
for i in range(len(deudores)):
    cliente= deudores[i].split(",")
    for x in range(len(cliente)):
            deudaind= cliente[4]
            deudaind= float(deudaind[1:])
    valores.append(deudaind)
    for x in range(len(valores)):
            total=0
            total=sum(valores)

print(total)







#2)

for i in range(len(deudores)):
    count=0
    cliente=deudores[i].split(",")
    for i in range(len(cliente)):
        sexo=cliente[3]

        if cliente[3] == "Female":
                count+1
        
print(sexo)
