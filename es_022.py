#CIARTANO ISABEL ES 22

#Scrivi una funzione parentesi_bilanciate(espressione) che usa una pila per verificare che le parentesi(,),[,],{,} siano correttamente bilanciate.

#Scrivi una funzione parentesi_bilanciate(espressione) che usa una pila per verificare che le parentesi(,),[,],{,} siano correttamente bilanciate.


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


def isOpen(c):
    return c == "(" or c == "[" or c == "{"


def isClose(c):
    return c == ")" or c == "]" or c == "}"


def isMatching(close, open):
    return (
        (close == ")" and open == "(")
        or (close == "]" and open == "[")
        or (close == "}" and open == "{")
    )


def parentesi_bilanciate(espressione):
    pila = None

    for c in espressione:
        if isOpen(c):
            if pila is None:
                pila = Nodo(c)
            else:
                pila = pila.push(c)

        elif isClose(c):
            if pila is None:
                return False

            if not isMatching(c, pila.valore):
                return False

            valore, pila = pila.pop()

    return pila is None


print(parentesi_bilanciate("(a+b)*[c-d]"))  # True
print(parentesi_bilanciate("{[()]}"))       # True
print(parentesi_bilanciate("([)]"))         # False
print(parentesi_bilanciate("((()"))         # False

#Domanda:Spiega a parole perché la pila è la struttura dati giusta per questo problema.

#La pila è la struttura dati giusta perché le parentesi devono essere controllate seguendo l’ordine LIFO (Last In, First Out).
#Quando trovi una parentesi aperta, la metti (push) nella pila. 
# Quando trovi una parentesi chiusa, devi controllare se corrisponde all’ultima parentesi aperta incontrata, 
# cioè quella in cima alla pila. In questo caso la togli (pop).