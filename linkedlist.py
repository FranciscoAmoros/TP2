
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

    def find_by_index(self, indice):
        
        if indice == 0:
            return self.head.data
        
        elemento = self.head
        
        for i in range(indice):
            if elemento.next:
                elemento = elemento.next

        return elemento.data
    
    def find(self, data):

        elemento_actual = self.head

        while elemento_actual:

            if elemento_actual.data == data:
                return elemento_actual

            elemento_actual = elemento_actual.next
    


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


    
    def imprimir(self):

        elemento_actual = self.head
        contador = 1

        while elemento_actual:
            print(f"{contador}. {elemento_actual.data.nombre} | {elemento_actual.data.tipo} | {elemento_actual.data.pc}")
            elemento_actual = elemento_actual.next
            contador += 1

    def obtener_ids(self):

        elemento_actual = self.head

        ids = []

        while elemento_actual:

            ids.append(elemento_actual.data.id)

            elemento_actual = elemento_actual.next

        return ids
    
    def ordenar_por_nombre(self):

        lista = []
        elemento_actual = self.head

        while elemento_actual:
            lista.append(elemento_actual.data)
            elemento_actual = elemento_actual.next

        n = len(lista)

        for i in range(n):
            for j in range(n - i - 1):
                if lista[j].nombre > lista[j + 1].nombre:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        self.head = None

        for pokemon in lista:
            self.append(pokemon)

    def ordenar_por_tipo(self):

        lista = []
        elemento_actual = self.head

        while elemento_actual:
            lista.append(elemento_actual.data)
            elemento_actual = elemento_actual.next

        n = len(lista)

        for i in range(n):
            minimo = i

            for j in range(i + 1, n):
                if lista[j].tipo < lista[minimo].tipo:
                    minimo = j

            lista[i], lista[minimo] = lista[minimo], lista[i]

        self.head = None

        for pokemon in lista:
            self.append(pokemon)

    def ordenar_por_poder_combate(self):

        lista = []
        elemento_actual = self.head

        while elemento_actual:
            lista.append(elemento_actual.data)
            elemento_actual = elemento_actual.next

        def quick_sort(lista):
            if len(lista) <= 1:
                return lista

            pivote = lista[len(lista) // 2]

            mayores = []
            iguales = []
            menores = []

            for pokemon in lista:
                if pokemon.pc > pivote.pc:
                    mayores.append(pokemon)
                elif pokemon.pc < pivote.pc:
                    menores.append(pokemon)
                else:
                    iguales.append(pokemon)

            return quick_sort(mayores) + iguales + quick_sort(menores)

        lista = quick_sort(lista)

        self.head = None

        for pokemon in lista:
            self.append(pokemon)
