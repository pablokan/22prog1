n = "1234567890"
j = ""
c = 0
for x in range(len(n)):
    j = n[len(n)-1-x] + j
    c += 1
    if c == 3 and x != len(n)-1:
        j = "." + j
        c = 0
print(j)
