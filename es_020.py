#CIARTANO ISABEL ES 20

#Implementa una classe Coda usando nodi autoreferenziali (senza usare list). La coda deve supportare:- enqueue(valore) — aggiunge in fondo
# - dequeue() — rimuove e restituisce il primo elemento (lancia IndexError se vuota)
# - peek() — restituisce il primo senza rimuoverlo
# - is_empty() — booleano
# - size() — numero di elementi
# - __str__—es. "[1 → 2 → 3]" (testa a sinistra)


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.successivo = None


class Coda:
    def __init__(self):
        self.testa = None
        self.coda = None
        self._size = 0

    def enqueue(self, valore):
        """Aggiunge un elemento in fondo alla coda."""
        nuovo = Nodo(valore)

        if self.is_empty():
            self.testa = nuovo
            self.coda = nuovo
        else:
            self.coda.successivo = nuovo
            self.coda = nuovo

        self._size += 1

    def dequeue(self):
        """Rimuove e restituisce il primo elemento."""
        if self.is_empty():
            raise IndexError("dequeue da coda vuota")

        valore = self.testa.valore
        self.testa = self.testa.successivo
        self._size -= 1

        if self._size == 0:
            self.coda = None

        return valore

    def peek(self):
        """Restituisce il primo elemento senza rimuoverlo."""
        if self.is_empty():
            raise IndexError("peek da coda vuota")

        return self.testa.valore

    def is_empty(self):
        """Restituisce True se la coda è vuota."""
        return self.testa is None

    def size(self):
        """Restituisce il numero di elementi."""
        return self._size

    def __str__(self):
        elementi = []
        corrente = self.testa

        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.successivo

        return "[" + " → ".join(elementi) + "]"


q = Coda()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)            # [1 → 2 → 3]
print(q.peek())     # 1
print(q.dequeue())  # 1
print(q)            # [2 → 3]
print(q.size())     # 2
print(q.is_empty()) # False