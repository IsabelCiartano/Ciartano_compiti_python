#CIARTANO ISABEL ES 15

#Senza eseguire il codice, scrivi l’output e spiega il meccanismo di ereditarietà.

#l'ereditarietà serve quando alcuni oggetti hanno dei metodi e degli attributi comuni a una classe e da essa ereditano aggiungendo poi dei metodi propri 
#della loro classe in questo caso l'auto aggiunge a veicolo il numero delle porte 

class Veicolo:
    def __init__(self, marca, velocita_max):
        self.marca = marca
        self.velocita_max = velocita_max
        self.velocita = 0
    def accelera(self, delta):
        self.velocita = min(self.velocita + delta, self.velocita_max)
    def __str__(self):
        return f"{self.marca} a {self.velocita} km/h"
    
class Auto(Veicolo):
    def __init__(self, marca, velocita_max, porte):
        super().__init__(marca,velocita_max)
        self.porte = porte
    def __str__(self):
        return super().__str__() + f" ({self.porte} porte)"
    
a = Auto("Fiat", 180, 5)
a.accelera(50)   #50
a.accelera(100) #150
a.accelera(100) #180
print(a)#fiat 180 (5)
print(isinstance(a, Veicolo))#true
print(isinstance(a, Auto))#true

#Domanda: Cosa fa super().__init__(...) e perché è necessario?
#super().__init__() serve per creare il costruttore della sotto classe è fondamentale per insierire anche gli attributi della sopra classe 
#e poi quelli della sotto classe, se non ci fosse il medoto la sottoclasse risulterebbe un oggetto incompleto

