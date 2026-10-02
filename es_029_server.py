#CIARTANO ISABEL ES 29

import socket


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    d = {}
    count = 0

    IP_PORTA = ("127.0.0.1", 9000)
    s.bind(IP_PORTA)

    BUFFER_SIZE = 4096

    print("server in ascolto .....")

    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE)

        stringa = dati.decode()
        count += 1

        if ip_porta_mittente in d:
            d[ip_porta_mittente] += 1
        else:
            d[ip_porta_mittente] = 1

        if count % 10 == 0:
            print("ricevuti 10 messaggi:")

            for ip in d:
                print(f"{ip} ha inviato {d[ip]} messaggi")

        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")

        if stringa.upper()=="STATS":
            messaggio=f"hai inviato :{d[ip_porta_mittente]} messaggi"
            s.sendto(messaggio.encode(),ip_porta_mittente)

        if stringa.upper() == "EXIT":
            s.sendto(f"ARRIVEDERCI".encode(),ip_porta_mittente)
            del d[ip_porta_mittente]

    s.close()


if __name__ == "__main__":
    main()