import random

class HashMap:
    def __init__(self, tamaño=10):
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

            for key, pokemon in self.buckets[i]:
                print(
                    f"  ID: {key} | "
                    f"Nombre: {pokemon.nombre} | "
                    f"Tipo: {pokemon.tipo} | "
                    f"CP: {pokemon.PC}"
                )
            
    def obtenerPokemonRandom(self): # (si no hay pokemones precargados en la pokedex se queda el loop infinito)

        done = False
        while not done:

            bucket = self.buckets[random.randint(0, 9)]

            if len(bucket) > 0:
                pokemon = bucket[random.randint(0, len(bucket)-1)]
                done = True

        return pokemon
    