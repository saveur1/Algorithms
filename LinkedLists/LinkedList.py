from Node import Node

#Initializing linked list class
class LinkedList:
    def __init__(self,node=None):
        self.length=0
        self.head=node
    
    #Method for returning length of linked list
    def length(self):
        current = self.head
        count = 0
        while current!=None:
            count+=1
            current = current.next
        
        return count
    
    #inserting node at front of linked list
    def insert_front(self,data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
        else:
            #make new node head of linked list
            newNode.next = self.head
            self.head = newNode
        #add 1 to length of linked list
        self.length+=1

    #inserting node at end of linked list
    def insert_end(self,data):
        newNode = Node(data=data)
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = newNode
        self.length+=1
    
    #method to display all nodes in linked list
    def display(self):
        current = self.head
        count = 1
        while current != None:
            print("item "+str(count)+": "+str(current.data))
            count+=1
            current = current.next

    
list = LinkedList()

#inserting new nodes both at front and at end of linked list
list.insert_front(12)
list.insert_front(15)
list.insert_front(30)
list.insert_end(50)
list.insert_end(80)



#printing list of nodes in linked list
list.display()

#printing linked list length
print("Length: "+str(list.length))