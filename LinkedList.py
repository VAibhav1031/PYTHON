class Node:
     def __init__(self,data):
          self.data=data
          self.next=None
          
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def inser_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node # point  the last_node next  to the new  node
    
    def delete_node(self, key):
            temp = self.head
    
            if temp and temp.data == key:
                self.head = temp.next
                temp = None
                return
    
            prev = None
            while temp and temp.data != key:
                prev = temp
                temp = temp.next
    
            if temp is None:
                return
    
            prev.next = temp.next
            temp = None
            
    def print_list(self):
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

sll=SinglyLinkedList()

#sll.insert_at_beginning(20)
sll.insert_at_end(14)
sll.insert_at_end(2)
sll.insert_at_end(6)
sll.inser_at_beginning(12)
sll.print_list()			
