#CIARTANO ISABEL ES 30

import socket
from threading import Thread, Lock

SERVER_ADDRESS=("127.0.0.1",9000)
BUFFER_SIZE=4096
client_connessi=[]
lock=Lock()

class ClientThread(Thread):
    def __init__(self,conn):
        super().__init__()
        self.conn=conn

        self.nickname=self.conn.recv(BUFFER_SIZE).decode()
        with lock:
            client_connessi.append((self.conn,self.nickname))
    def run(self):
        while True:
            dati=self.conn.recv(BUFFER_SIZE)

            if not dati:
                break
            messaggio=dati.decode()
            messaggio_completo=f"{self.nickname}:{messaggio}"

            with lock:
                for conn,nickname in client_connessi:
                    if conn !=self.conn:
                        conn.sendall(messaggio_completo.encode())
        with lock:
            client_connessi.remove((self.conn,self.nickname))
            notifica=f"{self.nickname} si è disconnesso"
            for conn,nickname in client_connessi:
                conn.sendall(notifica.encode())
        self.conn.close()
def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)
    server.listen()#ascolto per le connessioni 
    print("server in ascolto.....")


    while True:
        conn,addr=server.accept()
        thread=ClientThread(conn)
        thread.start()

if __name__=="__main__":
    main()
