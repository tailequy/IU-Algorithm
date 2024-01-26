# Implementation of Queue using array
class Queue:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return self.elements == []
    def size(self):
        return len(self.elements)
    def enQueue(self, newElement):
        self.elements.insert(0,newElement)
    def deQueue(self):
        return self.elements.pop()

q=Queue()
q.enQueue("A")
q.enQueue("B")
q.enQueue("C")
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
