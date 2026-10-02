#CIARTANO ISABEL ES 30

import socket
from threading import Thread

SERVER_ADDRESS=("127.0.0.1",9000)
BUFFER_SIZE=4096

class Receiver(Thread):

    def __init__(self, s):
        super().__init__()
        self.s=s
        self.daemon=True
    def run(self):
        while True:
            dati=self.s.recv(BUFFER_SIZE)
            if not dati:
                break
            messaggio=dati.decode()
            print("\n<- " + messaggio)
            print("-> ", end="", flush=True)#serve per evitare che gli input nella visualizzazione siano sbagliati es:-><- isa:bene

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    nick=input("inserisci nickname:")
    s.sendall(nick.encode())
    receiver=Receiver(s)
    receiver.start()

    while True:
        messaggio=input("->")
        if messaggio.upper()=="EXIT":
            break
        s.sendall(messaggio.encode())
    s.close()

if __name__=="__main__":
    main()