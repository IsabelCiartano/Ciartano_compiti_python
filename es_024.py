#CIARTANO ISABEL ES 24

#Completa il programma che simula il download parallelo di file. Aggiungi il codice indicato dai # TODO.
from threading import Thread, Lock
import time
import random

lock = Lock()
log = []
tot_mb=0

class Downloader(Thread):
   
    def __init__(self, nome_file, dimensione_mb):
        super().__init__()
        self.nome_file = nome_file
        self.dimensione_mb = dimensione_mb

    def run(self):
        # TODO: simula il download con time.sleep proporzionale alla dimensione
        # (usa dimensione_mb / 10 come durata in secondi)
        # TODO: al termine, aggiungi {"file": nome_file, "mb": dimensione_mb}
        # alla lista log in modo thread-safe (usa il lock)

        global tot_mb
        time.sleep(self.dimensione_mb/10)
        with lock:
            log.append({"file":self.nome_file,"mb":self.dimensione_mb})
            tot_mb+=self.dimensione_mb


def main():
    files = [
        ("video.mp4", 50),
        ("foto.jpg", 5),
        ("documento.pdf", 2),
        ("archivio.zip", 30),
        ("musica.mp3", 8),
    ]

    # TODO: crea un thread Downloader per ogni file e avviali tutti
    # TODO: aspetta che tutti i thread finiscano
    # TODO: stampa il log in ordine di completamento
    # TODO: stampa il totale dei MB scaricati
    
    download=[]

    for file in files:
        download.append(Downloader(file[0],file [1]))
    for d in download:
        d.start()
    for d in download:
        d.join()

    print(log)
    print(tot_mb)

if __name__ == "__main__":
    main()