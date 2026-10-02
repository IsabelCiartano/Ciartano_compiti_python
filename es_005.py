#CIARTANO ISABEL ES 5

#Senza e seguire il codice, scrivi l’output completo. Poi verifica.
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} è pari")
    else:
        print(f"{i} è dispari")
risultato = []
for i in range(10):
    if i % 3 == 0:
        risultato.append(i)
print(risultato)
x = 1
while x < 100:
    x *= 3
print(x)
#Domanda: Nel terzo blocco, quante iterazioni esegue il while? Giustifica la risposta.
#il ciclo while esegue 4 cicli pk la potenza di 3 al 4 ciclo diventa un numero già maggiore di cento 

#OUTPUT:
#1 èdispari 2 è pari,3 è dispari,4è pari,5 è dispari,3-6-9, 243