#CIARTANO ISABEL ES 9

#Scrivi una funzione conta_parole(testo) che riceve una stringa (un paragrafo) e restituisce un dizionario {parola:frequenza} 
#ignorando maiuscole/minuscole e punteggiatura (., ,, !, ?).

#Poi scrivi una funzione top_n(frequenze, n) che restituisce le n parole più frequenti come lista di tuple (parola,frequenza) in ordine decrescente.


def conta_parole(testo):
    for segno in ",.!?;:":
        testo = testo.replace(segno, "")
    parole=testo.split()
    d={}
    for p in parole:
        p.lower()
        if p in d:
            d[p]=d[p]+1
        else:
            d[p]=1
    return d
def top_n(frequenze, n):
    risultato = []

    for i in range(n):
        max_parola = ""
        max_freq = -1

        for parola in frequenze:
            if frequenze[parola] > max_freq:
                max_freq = frequenze[parola]
                max_parola = parola

        risultato.append((max_parola, max_freq))
        del frequenze[max_parola]

    return risultato
    
def main():
    testo=input("inserire il testo da analizzare ->")
    d=conta_parole(testo)
    print (d)
    top=top_n(
        d,3
    )
    print(top)

if __name__=="__main__":
    main()