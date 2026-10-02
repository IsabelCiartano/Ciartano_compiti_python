#CIARTANO ISABEL ES 14

#Implementa una classe Vettore2D che rappresenta un vettore nel piano. Deve supportare:
#• Costruttore __init__(self, x, y)
#• __str__ che stampa "Vettore(x, y)"
#• __add__ per sommare due vettori con +
#• __mul__ per moltiplicare per uno scalare con *
#• Metodo modulo() che restituisce la lunghezza del vettore
#• Metodo normalizza() che restituisce il vettore unitario
#• Metodo statico dot(v1, v2) per il prodotto scalare

import math
class Vettore2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"Vettore:({self.x},{self.y})"

    def __add__(self, other): #metodo speciale non lo richiamo con .add nel main ma con la somma a+b 
        return Vettore2D(self.x+other.x,self.y+other.y)
    def __mul__(self, other):# metodo speciale utilizzo la *
        return Vettore2D(self.x*other,self.y*other)
        
    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalizza(self):
        m = self.modulo()
        if m == 0:
            raise ValueError("Non è possibile normalizzare il vettore nullo.")# sollevo eccezione 
        return Vettore2D(self.x / m, self.y / m)

    def dot(v1, v2):# metodo statico pk è un metodo della classe non dell'oggetto 
        return v1.x * v2.x + v1.y * v2.y
    

a = Vettore2D(3, 4)
b = Vettore2D(1, 2)
print(a) # Vettore(3, 4)
print(a + b) # Vettore(4, 6)
print(a * 2) # Vettore(6, 8)
print(a.modulo()) # 5.0
print(Vettore2D.dot(a, b)) # 11