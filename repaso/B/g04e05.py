n = "23456789012"

q = ""
c = 0
for x in range(len(n)-1, -1, -1):
    c+=1 
    q = n[x] + q   
    if c == 3:
        q = "." + q
        c = 0
if q[0] == '.':
    q=q[1:]
print(q)
