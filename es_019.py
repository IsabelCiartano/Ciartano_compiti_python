#CIARTANO ISABEL ES 19

#Completa i metodi inserisci e cerca della classe Nodo. Non modificare la struttura della classe.
class Nodo:
    def __init__(self, valore, sx=None, dx=None):
        self.valore = valore
        self.sx = sx
        self.dx = dx
    def inserisci(self, valore):
        """
        Inserisce valore nell'albero rispettando la proprietà BST:
        valori minori a sinistra, maggiori a destra.
        Se valore è già presente, non fa nulla.
        """
        if valore <self.valore:
            if self.sx is None:
                self.sx=Nodo(valore)
            else:
                self.sx.inserisci(valore)
        elif valore >self.valore:
            if self.dx is None:
                self.dx=Nodo(valore)
            else:
                self.dx.inserisci(valore)
  
    def cerca(self, valore):
        """Restituisce True se valore è nell'albero, False altrimenti."""
        if valore == self.valore:
            return True
        elif valore < self.valore:
            if self.sx is None:
                return False
            else:
                return self.sx.cerca(valore)
        else:
            if self.dx is None:
                return False
            else:
                return self.dx.cerca(valore)
    def in_order(self):
        """Restituisce una lista con i valori in ordine crescente."""
        sx = self.sx.in_order() if self.sx else []
        dx = self.dx.in_order() if self.dx else []
        return sx + [self.valore] + dx
    
radice = Nodo(10)
for v in [5, 15, 3, 7, 12, 18, 1]:
    radice.inserisci(v)
print(radice.in_order())
print(radice.cerca(7))
print(radice.cerca(9))
# [1, 3, 5, 7, 10, 12, 15, 18]
# True
# False
#Domanda: Quanti confronti fa cerca(1) sull’albero costruito sopra? Descrivilo passo per passo.
#dalla radice 10 passa a 5 a sx poi a 3 a sx e poi arriva a 1 quindi fa 4 confronti 