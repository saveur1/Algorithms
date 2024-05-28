from Node import Node

'''Initializing linked list class'''
class LinkedList:
    def __init__(self,node=None):
        self.length=0
        self.head=node
    
    '''Method for returning length of linked list'''
    def length(self):
        current = self.head
        count = 0
        while current!=None:
            count+=1
            current = current.next
        
        return count
    
    '''inserting node at front of linked list'''
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

    '''inserting node at end of linked list'''
    def insert_end(self,data):
        newNode = Node(data=data)
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = newNode
        self.length+=1
    

    '''inserting node at any position in linked list'''
    def insert(self,position,data):
        #inserted wrong position
        if position < 0 or position > self.length:
            return None
        
        #position is starting of linked list
        if position == 0:
            self.insert_front(data)
            return
        
        #position is at end of linked list
        if position == self.length:
            self.insert_end(data)
            return
        
        #position is between start and end
        count = 0
        current = self.head
        while count < position-1:
            current=current.next
            count+=1
        #make new node point to following node then previous node to new inserting node
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode
        self.length += 1
    
    '''Deleting Node in first position'''
    def delete_front(self):
        if self.length == 0:
            print("Empty LinkedList")
        else:
            self.head = self.head.next
            self.length -= 1
    '''Deleting Node at end of list'''
    def delete_end(self):
        if self.length == 0:
            print("Empty LinkedList")
        else:
            #to get previous node:
            #make current node previous while next node to be current
            #terminate if there is no next node:
            #this keeps previous node and current node
            current = self.head
            prev_node = self.head
            while current.next != None:
                prev_node = current
                current = current.next
            prev_node.next = None
            self.length -= 1

    ''' DELETE FROM LINKED LIST WITH NODE'''
    def delete_node(self,node):
        if self.length == 0:
            raise ValueError("Linked list is Empty")
        
        current = self.head
        previous = None
        found = False
        while not found:
            if current == node:
                found = True
            elif current == None:
                raise ValueError("Node is not found")
            else:
                previous = current
                current = current.next
        
        if previous is None:
            self.head = current.next
        else:
            previous = current.next

        
        raise ValueError("Node not found")
    
    ''' DELETE FROM LINKED LIST WITH VALUE'''
    def delete_data(self,value):
        current = self.head
        previous = self.head
        while current.next != None or current.data == value:
            if current.data == value:
                previous.next = current.next
                self.length-=1
                return
            else:
                previous = current
                current = current.next
        
        print("There is no node found with that data")

    ''' DELETE FROM LINKED LIST WITH POSITION'''
    def delete(self,position):
        current = self.head
        previous = self.head
        count = 0

        if position < 0 or position > self.length-1:
            raise ValueError("Invalid position provided")
        elif position==0:
            self.delete_front()
        else:
            while current.next != None or count <= position:
                if count == position:
                    previous.next = current.next
                    self.length -= 1
                    return
                else:
                    previous = current
                    current = current.next
                    count = count + 1

                
    
    '''method to display all nodes in linked list'''
    def display(self):
        current = self.head
        count = 1
        while current != None:
            print("item "+str(count)+": "+str(current.data))
            count+=1
            current = current.next

    '''CLEARING ELEMENTS FROM LINKED LIST'''
    def clear(self):
        self.head = None
        self.length = 0
    

    
list = LinkedList()

#inserting new nodes both at front and at end of linked list
list.insert_front(12)
list.insert_front(15)
list.insert_front(30)
list.insert_end(50)
list.insert_end(80)
list.insert(5,100)


#deleting node
list.delete_front()
list.delete_end()
list.delete_data(80)
list.delete(2)

#printing list of nodes in linked list
list.display()

#printing linked list length
print("Length: "+str(list.length))