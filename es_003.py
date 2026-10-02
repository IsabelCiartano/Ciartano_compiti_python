#CIARTANO ISABEL ES 3

#Scrivi una funzione analizza_testo(frase) che riceve una stringa e restituisce un dizionario con: - "parole":
#numero di parole - "caratteri": numero di caratteri (spazi esclusi) - "vocali": numero di vocali (maiuscole e
#minuscole) - "parola_piu_lunga": la parola più lunga della frase
#Esempio:
#analizza_testo("la connessione di rete risulta lenta")
# → {"parole": 6, "caratteri": 31, "vocali": 14, "parola_piu_lunga": "connessione"}

def vocale(car):
    if car in "aeiouAEIOU":
        return True
    else:
        return False
    
def analizza_testo(frase):
   d={"parole":0,"caratteri":0,"vocali":0,"parola_piu_lunga":""}
   parole=frase.split()
   d["parole"]=len(parole)
   for p in parole:
       if len(d["parola_piu_lunga"])<len(p):
           d["parola_piu_lunga"]=p
   for c in frase :
       if (c.isalpha()):
           d["caratteri"]=d["caratteri"]+1
           if vocale(c):
               d["vocali"]=d["vocali"]+1
   return d


   

def main():
    frase=input("inserire la frase")
    d=analizza_testo(frase)
    print(d)

if __name__=="__main__":
    main()