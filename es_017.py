#CIARTANO ISABEL ES 17


#Il codice contiene errori.Trova li tutti e spiega cosa causava ciascuno.

class Contatore:
    totale =0 #variabile di classe
    def __init__(self,nome,inizio=0):
        nome = nome #manca self
        self.valore = inizio
        Contatore.totale=+1 #errorelogico sarebbe contatore.totale += 1
    def incrementa(self,n=1):
        self.valore+=n
    def resetta(self): #mancava self
        self.valore= 0
    def __str__(self):
        return f"Contatore{self.nome}: {self.valore}"

c1 =Contatore("A", 10)
c2 =Contatore("B")
c1.incrementa(5)
c2.incrementa()
print(c1)
print(c2)
print(f"Contatori creati:{Contatore.totale}") #atteso:2