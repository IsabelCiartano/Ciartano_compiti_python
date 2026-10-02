#CIARTANO ISABEL ES 2
#Il programma seguente contiene almeno 2 errori. Individuali, elencali come commenti e scrivi la versione
#corretta.

#def fibonacci(n)  manca il : 
   # a = 1
   # b = 1
   # risultato = []
   # for i in range(n):
        #risultato.append(a)
        #a, b == b, a + b  == confronta non assegna 
    #return risultato

#print(fibonacci(8)) # atteso: [1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n) : 
    a = 1
    b = 1
    risultato = []
    for i in range(n):
        risultato.append(a)
        a, b = b, a + b  
    return risultato
print(fibonacci(8))