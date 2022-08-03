from datetime import date

f = "29/02/2001"
d, m, a = f.split("/")
a = int(a)
m = int(m)
d = int(d)
date(a, m, d)


