from DoublyNode import Node

'''DEFINING DOUBLY LINKED LIST CLASS AS LINKED LIST'''
class LinkedList:
    def __init__(self,head = None,tail= None) -> None:
        self.head = head
        self.tail = tail
    
    '''Inserting at beginning of linked list'''
    def insert_front(self,data):
        #creating new node with incoming data
        newNode = Node(data)

        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    '''Display all data from doubly linked list'''
    def print(self):
        current = self.head
        count = 1
        while current != None:
            print("item %d = %d"%(count,current.data))
            count+=1
            current = current.next


list = LinkedList()
list.insert_front(15)
list.insert_front(11)
list.insert_front(4)
list.insert_front(19)

#printing data from linked list
list.print()