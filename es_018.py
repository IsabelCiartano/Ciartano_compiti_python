#CIARTANO ISABEL ES 18

#Crea una gerarchia di classi:
#Forma(classe base)
#Rettangolo
#Quadrato
# Cerchio
#•Forma ha metodi astratti area() e perimetro() e un metodo descrivi() che stampa tipo,area e perimetro.
#•Ogni sotto classe implementa area() e perimetro().
#•Quadrato eredita da Rettangolo e accetta un solo parametro lato.
#Crea una lista con almeno 2 istanze di ogni tipo e stampa la descrizione di ognuna.

import math
class Forma():
    def __init__(self):
        pass
    def area(self):
        pass
    def perimetro(self):
        pass
    def descrivi(self):
        return f"{self.__class__.__name__},{self.area()},{self.perimetro()}"

class Rettangolo(Forma):
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimetro(self):
        return (self.a+self.b)*2

class Quadrato(Rettangolo):
    def __init__(self,l):
        super().__init__(l,l)

class Cerchio(Forma):
    def __init__(self,r):
        super().__init__()
        self.r=r
    def area(self):
        return math.pi*self.r*self.r
    def perimetro(self):
        return 2*math.pi*self.r
forme = [
    Rettangolo(5, 3),
    Rettangolo(10, 4),
    Quadrato(5),
    Quadrato(8),
    Cerchio(3),
    Cerchio(6)
]

for forma in forme:
    print(forma.descrivi())
