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

    '''Method to insert node at end of linked list'''
    def insert_end(self,data):
        #create new node
        newNode = Node(data)

        #if there is nothing in linked list make new node head
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        
        #Else insert new node at the end of linked list
        current = self.head
        while current.hasNext():
            current = current.next

        current.next = newNode
        newNode.prev = current
        self.tail = newNode

        #############ALTERNATIVE OF INSERTING NODE AT TAIL IN LINKED LIST##########################
        # self.tail.next = newNode
        # newNode.prev = self.tail
        # self.tail = newNode
        

    '''Method to insert node in middle of linked list
    
        
    
    '''
    def insert(self,index,data):
        newNode = Node(data)

        #if index is 0 or nothing in linked list then
        if self.head == None or index == 0:
            self.insert_front(data)
            return
        
        #move to node to be inserted
        current = self.head
        previous = self.head
        count = 0
        while count < index and current.hasNext():
            previous = current
            current = current.next
            count+=1

        #insert node to require position
        if index > count:
            #insert node at the at end of linked list
            current.next = newNode
            newNode.prev = current
            self.tail = newNode
            return
        else:
            #insert node in middle
            newNode.next = current
            current.prev = newNode
            newNode.prev = previous
            previous.next = newNode

    '''Display all data from doubly linked list'''
    def print(self):
        current = self.head
        backward = self.tail
        count = 1
        print("FRONT LOOP         BACKWARD LOOP")
        while current != None and backward != None:
            print("item %d = %d        item %d = %d"%(count,current.data,count,backward.data))
            count+=1
            current = current.next
            backward = backward.prev


def main():
    list = LinkedList()
    list.insert_front(15)   #0
    list.insert_front(11)   #1
    list.insert_front(40)   #2
    list.insert_front(19)   #3
    list.insert_end(50)     #4
    list.insert_front(10)   #5
    list.insert_end(70)     #6
    list.insert(5,80)       #7

    #printing data from linked list
    list.print()


main()