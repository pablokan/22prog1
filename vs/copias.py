a = 1
b = a
a = 2
print(b)

l1 = [1, [1, 1]]
l2 = l1
l3 = l1.copy()
l1[0] = 2222
l1[1] = [3333, 33333]
print(l2, l3)
