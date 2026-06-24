import time

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
    
    queue = Queue()
    
    for pokemon in equipo:
        queue.enqueue(pokemon)
        print(f"curando: {pokemon.nombre}")
        time.sleep(2)
        
    for i in range(queue.size()):
        pokemon = queue.dequeue()
        print(f"pokemon curado: {pokemon}")
        
    
        
    