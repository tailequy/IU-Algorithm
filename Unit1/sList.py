#List (or singly linked list)
class Node:
    def __init__(self, elem):
        self.element = elem
        self.nextNode = None
    def getElement(self):
        return self.element
    def getNextNode(self):
        return self.nextNode
    def setElement(self, elem):
        self.element = elem
    def setNextNode(self, elem):
        self.nextNode = elem

#Supported operations
# LinkedList()constructs an empty list.
# isEmpty() returns True/False based on whether the list is empty or not.
# getLength() returns the number of elements in the list.
# addNode(element) adds a new element to the front of the list.
# deleteNode(element) removes the element from the list.
# searchNode(element) searches for the element’s item in the list, returning True/False.
# deleteNode and searchNode take O(n) time, the other operations take O(1) time

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
    def isEmpty(self):
        return (self.length==0)
    def getLength(self):
        return self.length
    def addNode(self,elem):
        temp=Node(elem)
        temp.setNextNode(self.head)
        self.head=temp
        self.length +=1
    def deleteNode(self, elem):
        lastNode = None
        thisNode = self.head
        found = False
        while not found:
            if (thisNode == None):
                break
            if thisNode.getElement() == elem:
                found = True
            else:
                lastNode = thisNode
                thisNode = thisNode.getNextNode()
        if (thisNode == None):
            print("Element not in list")
        elif lastNode == None:  # head node gets deleted
            self.head = thisNode.getNextNode()
            self.length -= 1
        else:
            lastNode.setNextNode(thisNode.getNextNode())
            self.length -= 1

    def searchNode(self, elem):
        thisNode = self.head
        found = False
        while ((not found) and (thisNode != None)):
            if thisNode.getElement() == elem:
                found = True
            else:
                thisNode = thisNode.getNextNode()
        return found
