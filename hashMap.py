class HashMap:
    def init(self, tamaño=10):
        self.tamaño = tamaño
        self.buckets = []
        for i in range(tamaño):
            self.buckets.append([])

    def funcion_hash(self, key):
        return hash(key) % self.tamaño

    def agregar(self, key, value):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                print("La key ya es existente.")
                return
        bucket.append([key, value])
        print(f"({key}, {value}) se agrego.")

    def buscar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                return par[1]
        return None

    def modificar(self, key, nuevo_value):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                par[1] = nuevo_value
                print(f"Value de {key} fue actualizado.")
                return
        print("Key no fue encontrada.")

    def eliminar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                bucket.remove(par)
                print(f"Key {key} eliminada.")
                return
        print("Key no encontrada.")

    def mostrar(self):
        print("\n=== HASH MAP ===")
        for i in range(self.tamaño):
            print(f"Bucket {i}: {self.buckets[i]}")

hashmap = HashMap()
hashmap.agregar(1, "Pikachu")
hashmap.agregar(11, "Charmander")
hashmap.agregar(21, "Bulbasaur")
hashmap.mostrar()
print("\nBuscar key 11:", hashmap.buscar(11))
hashmap.modificar(11, "Charizard")
print("Buscar key 11:", hashmap.buscar(11))
hashmap.eliminar(21)
hashmap.mostrar()