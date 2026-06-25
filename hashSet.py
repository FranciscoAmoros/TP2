import json

class HashSet:
    def __init__(self, tamaño=10):
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

        with open("medallas.json", "r", encoding="utf-8") as archivo:
            medallas_json = json.load(archivo)

        for medalla in medallas_json:
            if self.buscar(medalla["id"]):
                print(f"{medalla["id"]}: {medalla["nombre"]}")

