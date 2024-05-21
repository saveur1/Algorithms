#defining Node class for singly Linked List
class Node:
    #defining constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    #method for set data field of node
    def setData(self,data):
        self.data = data
    
    #method returning data field
    def getData(self):
        return self.data
    
    #method for setting next field
    def setNext(self,next):
        self.next = next

    #method for getting next pointer
    def getNext(self):
        return self.next
    
    #Returns true if data points to another node
    def hasNext(self):
        return self.next != None