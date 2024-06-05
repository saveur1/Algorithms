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
    
        case 1: No data in Linkedlist or we are inserting at beginning.
        case 2: Data to be inserted is located at the end of linkedlist
                .Data is located at end of linked list if
                    *After looping index is still greater than count
                    *That indicate that we are not replacing last element but we are inserting at end of list
        case 3: actually inserting between list
    
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

    '''DELETING NODE FROM DOUBLY LINKED LIST'''
    '''Deleting first node in doubly linked list'''
    def delete_front(self):
        if self.head == None:
            print("Nothing to delete")
            return
        else:
            self.head = self.head.next
            self.head.prev = None
    
    '''Deleting Node at end of linked list'''
    def delete_end(self):
        current = self.head
        previous = self.head

        if self.head == None:
            print("Nothing to delete")
            return
        
        #traverse through list
        while current.hasNext():
            previous = current
            current = current.next
        
        previous.next = None
        self.tail = previous

    '''Deleting node at any index in linked list'''
    def get_positioned_node(self,index):
        current = self.head
        if current == None:
            return None
        
        i=0
        while i<index:
            current = current.next
            
            if current == None:
                break
            
            i+=1

        return current
    
    def delete(self,index=0) :
        
        node_found = self.get_positioned_node(index)

        if node_found:
            #If Node to delete has previous then make previous point next to current node
            if node_found.prev:
                node_found.prev.next = node_found.next
            
            #If Node to delete has Next pointer then make Next pointer point to previous of node to delete
            if node_found.next:
                node_found.next.prev = node_found.prev
            
            #update tail pointer if deleted element was last in list
            if node_found.prev != None and node_found.prev.next == None:
                self.tail = node_found.prev
            
            #update head if deleted element was first in list
            if node_found.next != None and node_found.next.prev == None:
                self.head = node_found.next

            node_found = None
        

    '''Display all data from doubly linked list'''
    def print(self):
        current = self.head
        backward = self.tail
        count = 1
        print("FRONT LOOP         BACKWARD LOOP")
        while current != None or backward != None:
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
    list.insert(6,80)       #7

    #printing data from linked list
    list.print()
    print("********************************")

    #deleting nodes
    list.delete_front()
    list.delete_end()
    list.delete(5)
    list.delete(4)
    list.delete(2)
    #printing data from linked list
    list.print()


main()