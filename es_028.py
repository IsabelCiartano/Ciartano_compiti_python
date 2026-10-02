#CIARTANO ISABEL ES 28

import socket
from threading import Thread, Event

SERVER_ADDRESS = ("127.0.0.1", 5000)
BUFFER_SIZE = 4096

stop_event = Event()


class Receiver(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.daemon = True  # si chiude automaticamente con il programma

    def run(self):
        # TODO: ricevi messaggi in loop finché stop_event non è settato
        # stampa ogni messaggio ricevuto con il prefisso "<- "
        while not stop_event.is_set():#non è settato quindi può continuare a ricevere
            messaggio,_=self.s.recvfrom(BUFFER_SIZE)
            print(f"<- {messaggio.decode()}")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # TODO: crea e avvia il thread Receiver
    reciever=Receiver(s)
    reciever.star()

    while True:
        messaggio = input("-> ")
        s.sendto(messaggio.encode(), SERVER_ADDRESS)

        if messaggio.upper() == "EXIT":
            # TODO: setta stop_event e interrompi il loop
            stop_event.set() #segnala al thread che deve terminare
            break

    s.close()


if __name__ == "__main__":
    main()

#Domanda: Perché il thread Receiver è impostato come daemon = True? Cosa succederebbe senza?
#serve per quando il main()finisce e il programma principale termina anche il thread si chiude automaticamente,
#se fosse impostato a false python aspetteebbe che anche quel thread termini prima di chiudere completamente il programma 