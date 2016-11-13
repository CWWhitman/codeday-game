print "test"
l = []
l.append("".join(["1" for _ in range(30)]))
for a in range(10):
    l.append("".join(["0" for _ in range(25)]) +"11111")
for a in range(1):
    l.append("0" * 5 + "1" * 25)
for a in range(2):
    l.append("".join(["0" for _ in range(10)]) +"1" * 20)
l.append("".join(["1" for _ in range(30)]))
#x,y
for a in range(6):
    p = list(l[a])
    p[20] = "1"
    l[a] = "".join(p)
