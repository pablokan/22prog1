l1 = set([1,2,3,4])
l2 = set([0, 2, 4, 2])
print(l1.intersection(l2))
l2 = list(set(l2))

for eL1 in l1:
    for eL2 in l2:
        if eL1 == eL2:
            print(eL1)

for eL1 in l1:
    if eL1 in l2:
        print(eL1)

