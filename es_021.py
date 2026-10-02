#CIARTANO ISABEL ES 21

#Senza eseguire il codice, traccia lo stato della pila dopo ogni operazione e scrivi l’output

class Nodo:
    def __init__(self, valore, next=None):
        self.valore = valore
        self.next = next

    def push(self, v):
        return Nodo(v, self)

    def pop(self):
        return self.valore, self.next

    def __str__(self):
        els, n = [], self

        while n:
            els.append(str(n.valore))
            n = n.next

        return " → ".join(els)


pila = Nodo(1)
pila = pila.push(2)
pila = pila.push(3)

print(pila) #1 ->2 3

v, pila = pila.pop()
print(v, "|", pila) #3 | 1 2

pila = pila.push(10) 
pila = pila.push(20)

print(pila)#1 ->2 10 20

v, pila = pila.pop()
print(v, "|", pila)#20|1 ->2 10