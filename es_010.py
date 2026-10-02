#CIARTANO ISABEL ES 10

#Il programma deve costruire un dizionario {provincia: [città]} da una lista di tuple. Contiene errori logici e di sintassi.

def raggruppa_per_provincia(dati):
    risultato = {}

    for citta, provincia in dati:
        if provincia not in risultato:
            risultato[provincia]=[citta] #era sbagliato = citta devo creaare la lista quindi [citta]
        else:
            risultato[provincia].append(citta)

    return risultato


dati = [
    ("Torino", "TO"),
    ("Moncalieri", "TO"),
    ("Milano", "MI"),
    ("Sesto", "MI"),
    ("Genova", "GE")
]

print(raggruppa_per_provincia(dati))

# atteso:
# {
#     'TO': ['Torino', 'Moncalieri'],
#     'MI': ['Milano', 'Sesto'],
#     'GE': ['Genova']
# }