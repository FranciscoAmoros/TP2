class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
        if self.size() > 6:
            self.stack.pop(0)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
def main():

    global stack

    stack = Stack()


def transferir(pokemon):

    global stack

    stack.push(pokemon)

def deshacerTransferencia():

    global stack

    return stack.pop()