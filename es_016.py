#CIARTANO ISABEL ES 16

#Crea una clsse Studente con: - attributi: nome, cognome, voti (lista, inizialmen te vuota) - metodo
#aggiungi_voto(voto) — aggiunge un voto alla lista - metodo media() — restituisce la media, o None se
#non ci sono voti - metodo promosso() — restituisce True se media >= 6 - __str__ — es. "Rossi Mario — media:
#7.3 (promosso)"

#Crea un a classe Registro che con tiene una lista di studenti e fornisce: - aggiungi_studente(studente) - 
# classifica() — lista di studenti ordinati per media decrescente - insufficienti() — lista di studenti non promossi
# salva_csv(nome_file) — salva nome, cognome, media su file CSV

class Studente:
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
        self.voti=[]
    def aggiungi_voto(self,voto):
        self.voti.append(voto)
    def media(self):
        media=0
        if self.voti:
            for v in self.voti:
                media=media+v
            return media/len(self.voti)
        else:
            return None
    def promosso(self):
        if self.media()>=6:
            return True
        else:
            return False
    def __str__(self):
        promosso="Bocciato"
        if self.promosso():
            promosso="promosso"
        return f"{self.nome} {self.cognome} media:{self.media()} ({promosso})"
    
    #metodo non richiesto cercato per stampare la lista non con il nome dell'oggetto ma con __str__
    def __repr__(self):
        return self.__str__()
    #-----------------------------------------------------------------------------------------------

class Registro:
    def __init__(self):
        self.studenti=[]
    def aggiungi_studente(self,studente):
        self.studenti.append(studente)
    def classifica(self):
        classifica = self.studenti[:]

        for i in range(len(classifica)):
            for j in range(len(classifica) - 1 - i):
                if classifica[j].media() < classifica[j + 1].media():
                    classifica[j], classifica[j + 1] = classifica[j + 1], classifica[j]

        return classifica
    def insufficenti(self):
        insuff=[]
        for s in self.studenti:
            if s.promosso()==False:
                insuff.append(s)
        return insuff
    def salva_csv(self,nome_file):
        file=open(nome_file,"w")
        for s in self.studenti:
            file.write(f"{s.nome} {s.cognome} media:{s.media()}\n")
        file.close
    



s=Studente("isabel","ciartano")
s.aggiungi_voto(7)
s.aggiungi_voto(8)
print(s)
s2=Studente("mario","rossi")
s2.aggiungi_voto(4)
s2.aggiungi_voto(5)
print(s2)
r=Registro()
r.aggiungi_studente(s)
r.aggiungi_studente(s2)
print(r.classifica())
print(r.insufficenti())
r.salva_csv("./studenti.csv")
        
                


