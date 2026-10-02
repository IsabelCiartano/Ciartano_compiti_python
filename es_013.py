#CIARTANO ISABEL ES 13

#Hai una lista di rilev azioni nel formato:
rilevazioni = [
{"stazione": "Torino", "ora": 8, "temp": 18.2, "umidita": 65},
{"stazione": "Torino", "ora": 12, "temp": 24.5, "umidita": 52},
{"stazione": "Milano", "ora": 8, "temp": 16.0, "umidita": 70},
{"stazione": "Milano", "ora": 12, "temp": 22.1, "umidita": 58},
{"stazione": "Torino", "ora": 16, "temp": 26.3, "umidita": 48},
{"stazione": "Milano", "ora": 16, "temp": 23.8, "umidita": 55},
]
#Scrivi funzioni che calcolano: 1. La temperatura media per stazione 2. La rilevazione con temperatura massima
#(restituisci l’intero dizionario) 3. Tutte le rilevazioni dove l’umidità è sopra una soglia passata come parametro,
#ordinate per temperatura decrescente


def temp_media(rilevazioni):
    medie={}
    cont_TO=0
    cont_MI=0
    media_TO=0
    media_MI=0

    for r in rilevazioni:
        if r["stazione"]=="Torino":
            media_TO+=r["temp"]
            cont_TO=cont_TO+1
        elif  r["stazione"]=="Milano":
            media_MI=media_MI+r["temp"]
            cont_MI=cont_MI+1

    medie["milano"]=media_MI/cont_MI
    medie["torino"]=media_TO/cont_TO
    return medie

def val_max(rilevazioni):
    massimo=0
    mass_d={}
    for r in rilevazioni:
        if r["temp"]>massimo:
            massimo=r["temp"]
            mass_d=r
    return mass_d

def umidita(rilevazioni,soglia):
    umidita=[]
    for r in rilevazioni:
        if r["umidita"]>soglia:
            umidita.append(r)
    for i in range(len(umidita)):
        for j in range(len(umidita) - 1 - i):
            if umidita[j]["temp"] < umidita[j + 1]["temp"]:
                temp = umidita[j]
                umidita[j] = umidita[j + 1]
                umidita[j + 1] = temp
    return umidita


def main():
    medie=temp_media(rilevazioni)
    print(medie)
    massimo=val_max(rilevazioni)
    print(massimo)
    soglia=int(input("che soglia di umidita vuoi impostare->"))
    um=umidita(rilevazioni,soglia)
    print(um)
    
if __name__=="__main__":
    main()
