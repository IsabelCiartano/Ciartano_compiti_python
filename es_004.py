#CIARTANO ISABEL ES 4

#Scrivi un programma che chiede all’utente una temperatura e l’unità (C, F, o K) e la converte nelle altre due
#unità. Usa funzioni separate per ogni con versione. Gestisci il caso in cui l’utente inserisca un’unità non valida.
#Formule: - °F = °C × 9/5 + 32 - K = °C + 273.15

def main():
    t = float(input("Inserisci la temperatura: "))
    unita = input("Inserisci l'unità (C, F, K): ").upper()

    if unita=="C" or unita == "K" or unita == "F":
        if unita=="C":
            unita_F=t*(9/5)+32
            unita_K=t+273.15
            print(f"conversioni :{unita_F} F - {unita_K} K")
        elif unita=="F":
            unita_C=(t-32)*(5/9)
            unita_K=(t-32)*(5/9)+273.15
            print(f"conversioni :{unita_C} C - {unita_K} K")
        elif unita=="K":
            unita_C=t-273.15
            unita_F=(t-273.15)*(9/5)+32
    else:
        print("unità di misura non valida ")
if __name__=="__main__":
    main()