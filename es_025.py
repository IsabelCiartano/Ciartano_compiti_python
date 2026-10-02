#CIARTANO ISABEL ES 25


#1. Scrivi un programma che riproduce una race condition: 5 thread incrementano una variabile condivisa
#contatore per 1000 volte ciascuno, separando lettura e scrittura con un time.sleep molto breve. Verifica
#che il risultato sia sbagliato (< 5000).
#2. Correggi il programma usando un Lock (mutex) in modo che il risultato sia sempre esattamente 5000.
#3. Scrivi nei commenti: qual è la differenza di tempo di esecuzione tra le due versioni? Perché il mutex
#rallenta?
from threading import Thread,Lock
import time

totale=0
lock=Lock()

class thread(Thread):
    def __init__(self):
        super().__init__()
        

    def run(self):
        global totale
        with lock:
            for n in range(1000):
                time.sleep(0.1)
            
                totale+=1
            print("finito")

def main():
    t1=thread()
    t2=thread()
    t3=thread()
    t4=thread()
    t5=thread( )

    for t in[t1,t2,t3,t4,t5]:
        t.start()

    for t in [t1,t2,t3,t4,t5]:
        t.join()

    print(totale)


if __name__=="__main__":
    main()

#il mutex rallenta l'esecuzione perchè i thread devono aspettare il loro turno per accedere alla risorsa collettiva mentre senza accedevano senza aspettare ma 
#ciò portava a un risultato sbagliato alla fine 