#CIARTANO ISABEL ES 27


#SERVER
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5000))

print("Server pronto")

while True:
    dati, addr = s.recvfrom(1024)

    msg = dati.decode()

    print(f"Da {addr}: {msg}")

    risposta = msg.upper()

    s.sendto(risposta.encode(), addr)

    if msg == "exit":
        break

s.close()

#CLIENT
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ("127.0.0.1", 5000)

while True:
    msg = input("-> ")

    s.sendto(msg.encode(), server)

    dati, _ = s.recvfrom(1024)

    print(f"<- {dati.decode()}")

    if msg == "exit":
        break

s.close()

#1. Cosa fa il server con ogni messaggio ricevuto?
#il server riceve il messaggio fa una print del messaggio ricevuto e da chi, inseguito lo trasforma in maiuscolo e lo rimanda al client 

#2. Perché il server usa "0.0.0.0" e non "127.0.0.1" nel bind?
#perchè facendo il bind su 0.0.0.0 il server si mette in ascolto su tutte le interfacce di rete,
#con 127.0.0.1 accetterebbe solo connessioni dalla stessa macchina local host 
#cioè il server può ricevere messaggi sulla porta anche da altri dispositivi 

#3. Cosa succede se avvi i due client contemporaneamente? Il server regge?
#il server regge e può gestire due client contemporaneamente ma essendo UDP non ha una connessione separata
#per ogni client 
#il messaggio arriva da un qualunque client e grazie alla variabile addr sa da dove proviene 
#il server però gestisce i messaggi uno alla volta nell'ordine in cui arrivano non contemporaneamente tramite un thread 

#4. Qual è la differenza tra UDP e TCP? Questo server funzionerebbe con TCP senza modifiche?
#la differenza principale tra UDP e TCP è la connessione, TCP è orientato alla connessione cioè stabilisce connessione tra client
#e server, mentre UDP no .
#inoltre TCP garantisce lìordine dei data e la consegna, nel codice untilizza SOCK_STREAM invece che SOCK_DGRAM
#nonostante ciò anche se cambiassimo quasto nel codice non sarebbe sufficente per passare a un server TCP infatti bisognerebbe anche mettersi in ascolto ed accettare 
#la connessione con il client per far in modo che funzioni 