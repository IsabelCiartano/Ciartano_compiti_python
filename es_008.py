#CIARTANO ISABEL ES 8

#Scrivi l’output di ogni blocco. Poi verifica.

# Blocco A
l = [10, 20, 30, 40, 50]

l.append(60)
l.pop(2)

print(l)
print(l[1:4])
#10,20,40,50,60
#20,40,50

# Blocco B
d = {"a": 1, "b": 2, "c": 3}

d["d"] = 4
del d["a"]

print(d)
print(list(d.keys()))
print(sum(d.values()))
#b:2,c:3,d:4
#b,c,d
#9

# Blocco C
nomi = ["Alice", "Bob", "Carlo", "Diana"]

for i, nome in enumerate(nomi):
    if i % 2 == 0:
        print(nome.upper())
    else:
        print(nome.lower())

#ALICE,bob,CARLO,diana
