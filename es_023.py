#CIARTANO ISABEL ES 23

#Considera questo programma. Rispondi alle domande senza eseguirlo.

from threading import Thread
import time

risultati = []

class Lavoratore(Thread):
    def __init__(self, nome, durata):
        super().__init__()
        self.nome = nome
        self.durata = durata

    def run(self):
        time.sleep(self.durata)
        risultati.append(self.nome)
        print(f"{self.nome} ha finito")

t1 = Lavoratore("A", 0.3)
t2 = Lavoratore("B", 0.1)
t3 = Lavoratore("C", 0.2)

for t in [t1, t2, t3]:
    t.start()

for t in [t1, t2, t3]:
    t.join()

print("Ordine di completamento:", risultati)
#1. In quale ordine verranno stampati i messaggi “ha finito”?
#i messaggi verranno stampati con ordine b c a 
#2. Cosa contiene risultati alla fine? In quale ordine?
#contiene bca
#3. Cosa succederebbe se rimuovessi tutti i t.join()? Il programma darebbe lo stesso risultato?
#se rimuovessimo il t join il risultato sarebbe diverso perchè il thread non si ricongiunge con il main e quindi non termina 
#4. Perché risultati è una lista globale e non locale al thread?
#è globale perchè è accessibile a tutti i thread fossse interna al thread solo esso potrebbe accederci 
