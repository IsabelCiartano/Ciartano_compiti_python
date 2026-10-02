#CIARTANO ISABEL ES 11

#Scrivi un programma a menu (loop con while) che gestisce una rubrica in memoria (dizionario {nome: numero}):
#• 1 — Aggiungi contatto
#• 2 — Cerca contatto per nome (anche parziale)
#• 3 — Elimina contatto
#• 4 — Mostra tutti i contatti in ordine alfabetico
#• 5 — Salva la rubrica su file rubrica.txt e termina
#Al riavvio del program ma, la rubrica deve e sser e carica ta da l file se e siste.

def main():
    try:
        file = open("./rubrica.txt", "r")
        for riga in file:
            nome, numero = riga.strip().split(";")
            rubrica[nome] = numero

        file.close()
    except FileNotFoundError:
        rubrica = {}
    while(True):
        print("• 1 — Aggiungi contatto\n• 2 — Cerca contatto per nome (anche parziale)\n• 3 — Elimina contatto\n• 4 — Mostra tutti i contatti in ordine alfabetico\n• 5 — Salva la rubrica su file rubrica.txt e termina")
        scelta=int(input("scelta->"))
        if scelta==1:
            nome=input("inserire il nominativo ->")
            numero=int(input("inserire il numero->"))
            rubrica[nome]=numero
        elif scelta==2:
            cerca=input("che contatto si vuole cercare? ->")
            for p in rubrica:
                if cerca in p :
                    print(f"nome:{p} numero: {rubrica[p]}")
        elif scelta==3:
            cerca=input("che contatto si vuole eliminare? ->")
            for p in rubrica:
                if cerca == p :
                    cancellare=p
            del rubrica[cancellare]
            print("contatto eliminato")
        elif scelta==4:
            for p in sorted(rubrica):
                print(f"nome:{p} numero:{rubrica[p]}")
        elif scelta==5:
            file = open("./rubrica.txt", "w")

            for nome in rubrica:
                file.write(nome + ";" + str(rubrica[nome]) + "\n")
            file.close()
            break


    
if __name__=="__main__":
    main()