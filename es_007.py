#CIARTANO ISABEL ES 7

#Completa le funzioni mancanti. Non modificare la firma dei metodi né il main.
import random
import string


def genera_password(lunghezza, usa_maiuscole=True, usa_numeri=True, usa_simboli=False):
    """
    Genera una password casuale.

    - lunghezza: numero di caratteri
    - usa_maiuscole: include lettere maiuscole
    - usa_numeri: include cifre
    - usa_simboli: include !@#$%

    Restituisce la password come stringa.
    """
    caratteri=""
    pw=""
    if usa_maiuscole:
        caratteri+="ABCDEFGHIJKMLNOPQRTSUV"
    if usa_numeri:
        caratteri+="1234567890"
    if usa_simboli:
        caratteri+="!£$%&._-#"

    for i in range(lunghezza):
        pw+=random.choice(caratteri)

    return pw


def valuta_forza(password):
    """
    Restituisce "debole", "media" o "forte" in base a:

    - debole: solo lettere minuscole o lunghezza < 8
    - forte: lunghezza >= 12 e contiene maiuscole, numeri e simboli
    - media: tutto il resto
    """
    maiuscole=False
    simboli=False
    numeri=False
    for c in password:
        if c in "ABCDEFGHIJKMLNOPQRTSUV":
            maiuscole=True
        elif c in "1234567890":
            numeri=True
        elif c in "!£$%&._-#":
            simboli=True
    if len(password)<8 or maiuscole==False:
        return "debole"
    if len(password)>=12 and simboli==True and maiuscole==True and numeri==True:
        return "forte"
    else:
        return "media"


def main():
    pw = genera_password(
        12,
        usa_maiuscole=True,
        usa_numeri=True,
        usa_simboli=True
    )

    print(f"Password: {pw}")
    print(f"Forza: {valuta_forza(pw)}")


if __name__ == "__main__":
    main()