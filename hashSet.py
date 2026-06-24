class HashSet:
    def init(self, tamaño=10):
        self.tamaño = tamaño
        self.buckets = []
        for i in range(tamaño):
            self.buckets.append([])

    def funcion_hash(self, key):
        return hash(key) % self.tamaño

    def agregar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        if key not in bucket:
            bucket.append(key)
            print(f"{key} agregado.")
        else:
            print(f"{key} ya esta en el hash set.")

    def eliminar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        if key in bucket:
            bucket.remove(key)
            print(f"{key} eliminado.")
        else:
            print(f"{key} no encontrado.")

    def buscar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        return key in bucket

    def mostrar(self):
        print("\nHASH SET:")
        for i in range(self.tamaño):
            print(f"Bucket {i}: {self.buckets[i]}")

hashset = HashSet()
hashset.agregar(30)
hashset.agregar(15)
hashset.agregar(40)
hashset.agregar(30) 
hashset.mostrar()
print("\nBuscar 25:", hashset.buscar(25))
print("Buscar 50:", hashset.buscar(50))
hashset.eliminar(25)
hashset.mostrar()