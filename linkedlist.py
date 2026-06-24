
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        nuevo_elemento = Node(data)

        if self.head is None:
            self.head = nuevo_elemento
            return

        elemento_actual = self.head

        while elemento_actual.next:
            elemento_actual = elemento_actual.next

        elemento_actual.next = nuevo_elemento
    
    def find(self, data):

        """

        if indice == 0:
            return self.head
        
        elemento = self.head
        
        for i in range(indice):
            if elemento.next:
                elemento = elemento.next

        return elemento
        """

        elemento_actual = self.head

        while elemento_actual:

            if elemento_actual.data == data:
                return elemento_actual

            elemento_actual = elemento_actual.next
    
    def ordenar(self): # bubble sort

        movio = True

        while movio:

            movio = False
            actual = self.head

            while actual and actual.next:

                if actual.data > actual.next.data:

                    actual.data, actual.next.data = (
                        actual.next.data,
                        actual.data
                    )

                    movio = True

                actual = actual.next

    def delete(self, data):

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        elemento_actual = self.head

        while elemento_actual.next:

            if elemento_actual.next.data == data:
                elemento_actual.next = elemento_actual.next.next
                return

            elemento_actual = elemento_actual.next

    def imprimir(self):

        elemento_actual = self.head

        while elemento_actual.next:
            print(elemento_actual.data)
            elemento_actual = elemento_actual.next

    def size(self):

        if self.head is None:
            return 0
        
        contador = 1

        elemento_actual = self.head
        
        while elemento_actual.next:
            elemento_actual = elemento_actual.next
            contador += 1

        return contador

    def is_empty(self):


        if self.head == None:
            return True
        
    def insert(self, data, posicion):

        nuevo_elemento = Node(data)

        # Insertar al principio
        if posicion == 0:
            nuevo_elemento.next = self.head
            self.head = nuevo_elemento
            return

        elemento_actual = self.head
        indice = 0

        while elemento_actual and indice < posicion - 1:
            elemento_actual = elemento_actual.next
            indice += 1

        # Posición inválida
        if elemento_actual is None:
            return

        nuevo_elemento.next = elemento_actual.next
        elemento_actual.next = nuevo_elemento

    def get_tail(self):

        elemento_actual = self.head

        if elemento_actual.next == None:
            return elemento_actual
        
        while elemento_actual.next:
            elemento_actual = elemento_actual.next

        return elemento_actual

    def reverse(self):

        anterior = None
        actual = self.head

        while actual:

            siguiente = actual.next

            actual.next = anterior

            anterior = actual
            actual = siguiente

        self.head = anterior

    def has_cycle(self):

        tortuga = self.head
        liebre = self.head

        while liebre and liebre.next:

            tortuga = tortuga.next
            liebre = liebre.next.next

            if tortuga == liebre:
                return True

        return False