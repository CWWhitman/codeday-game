print "test"
l = []
l.append("".join(["1" for _ in range(30)]))
for a in range(10):
    l.append("".join(["0" for _ in range(25)]) +"11111")
for a in range(3):
    l.append("".join(["0" for _ in range(10)]) +"1" * 20)
l.append("".join(["1" for _ in range(30)]))

