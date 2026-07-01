import time

base_de_datos = None

def main(hashmap):
    global base_de_datos
    base_de_datos = hashmap

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    

def curar(equipo):

    global base_de_datos
    
    queue = Queue()

    if not equipo:
        print("no hay pokemones en tu equipo.")
        return
    
    for pokemon in equipo:
        queue.enqueue(pokemon)
        print(f"curando: {pokemon.nombre}")

        pokemon.pc = base_de_datos.buscar(pokemon.id).pc
        
        time.sleep(2)
        
    for i in range(queue.size()):
        pokemon = queue.dequeue()
        print(f"pokemon curado: {pokemon.nombre}")
        
    
        
    