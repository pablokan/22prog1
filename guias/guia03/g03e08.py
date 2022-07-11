#n = [11, 22, 33, 44, 55]
n = ["hola", "como", "te", "va"]
for x in range(len(n)//2):
    aux = n[x]
    n[x] = n[len(n)-1-x]
    n[len(n)-1-x] = aux

print(n)
