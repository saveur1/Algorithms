#defining class of doubly linked list
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

    '''Defining setters and getters'''
    #Data,setters and getters
    def setData(self,data):
        self.data = data
    
    def getData(self):
        return self.data
    
    #previous pointer, setters and getters
    def setPrev(self,prev):
        self.prev = prev
    
    def getPrev(self):
        return self.prev
    
    def hasPrev(self):
        return self.prev != None
    

    #next pointer, setters and getters
    def setNext(self,next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None
    
    '''stringfying an object'''
    def __str__(self):
        return "Node[data=%s]" % (self.data)
    
