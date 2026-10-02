#CIARTANO ISABEL ES 29

import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    DESTINATARIO = ("127.0.0.1", 9000)
    BUFFER_SIZE = 4096

    while True:
        messaggio = input("-> ")

        s.sendto(messaggio.encode(), DESTINATARIO)

        # STATS ed EXIT prevedono una risposta dal server
        if messaggio.upper() == "STATS" or messaggio.upper() == "EXIT":
            risposta, _ = s.recvfrom(BUFFER_SIZE)
            print("<- " + risposta.decode())

        # Dopo EXIT chiudo il client
        if messaggio.upper() == "EXIT":
            break

    s.close()


if __name__ == "__main__":
    main()