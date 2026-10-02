#CIARTANO ISABEL ES 6

#Crea un file studenti.csv con almeno 10 righe nel formato:
#Nome,Cognome,Voto1,Voto2,Voto3
#Mario,Rossi,7,8,6

#Scrivi un programma che: 1. Legge il file 2. Calcola la media di ogni studente 3. Stampa l’elenco ordinato per
#media (dal più alto al più basso) 4. Stampa il nome dello studente con la media più alta 5. Stampa quanti studenti hanno media inferiore a 6

file=open("./studenti.csv","r")
def media(studenti):
    risultato = []

    for studente in studenti:
        dati = studente.split(",")

        nome = dati[0]
        cognome = dati[1]
        voto1 = int(dati[2])
        voto2 = int(dati[3])
        voto3 = int(dati[4])

        media = (voto1 + voto2 + voto3) / 3

        risultato.append([nome, cognome, media])

    return risultato

def ordina(studenti):
    n = len(studenti)

    for i in range(n):
        massimo = i

        for j in range(i + 1, n):
            if studenti[j][2] > studenti[massimo][2]:
                massimo = j

        temp = studenti[i]
        studenti[i] = studenti[massimo]
        studenti[massimo] = temp

def elenco_stud(studenti):
    for s in studenti:
        print(s)
def migliore(studenti):
    print(f"Media più alta:{studenti[0]}")
def insufficenze(studenti):
    insufficenti=[]
    for s in studenti:
        if s[2] <6:
            insufficenti.append([s[0],s[2]])
    return insufficenti

def main():
   
    righe=file.readlines()
    file.close()
    print(righe)
    studenti=media(righe)
    ordina (studenti)
    elenco_stud(studenti)
    migliore(studenti)
    s_inssuff=insufficenze(studenti)
    print(s_inssuff)

if __name__=="__main__":
    main()