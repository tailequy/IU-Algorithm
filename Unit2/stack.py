# Implementation of Stack using array
class Stack:
    def __init__(self):
        self.elements = [] #Initialized to empty list

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def topOfStack(self):
        return self.elements[len(self.elements)-1]

    def push(self, newElement):
        self.elements.append(newElement)

    def pop(self):
        return self.elements.pop()#Python's in-built pop


s=Stack()
s.push("D")
s.push("C")
print(s.pop())
s.push("B")
s.push("A")
print(s.pop())
print(s.pop())
print(s.pop())