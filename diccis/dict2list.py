mylist = ['1', '2', '3', '3', '1', '4']

results = list({k:"poronga" for k in mylist})
print(results)


d = dict.fromkeys(mylist)
print(d)
results = list(d)
print(results)


n = {"nombre": "Juan", "edad": 33, "nombre": "Pedro"}
print(list(n))