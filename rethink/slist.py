class  Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
       new_node=Node(data)
       if not self.head:
           self.head=new_node 
       else:
           curr=self.head
           while curr.next is not None:
               curr=curr.next
           curr.next=new_node
    def  traverse(self):
        if not self.head:
            print("empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=",")
                curr=curr.next
    def find(self,data):
        if not self.head:
            print("empty")
        else:
            curr=self.head
            while curr is not None:
                if curr.val==data:
                  print("found",end=",")
                curr=curr.next
                
    def delete(self,data):
        if not self.head:
                print("empty")
        elif self.head.val==data:
             curr=self.head
             self.head=curr.next
            
        else:    
            curr=self.head
            prev=self.head
            while curr is not None:
                if curr.val==data:
                    prev.next=curr.next
                    curr.next=None
                prev=curr
                curr=curr.next
            
        
    
sl=SinglyLinkedList()
sl.append(1)
sl.append(3)
sl.append(4)
sl.append(5)
sl.append(12)
sl.append(13)
sl.append(14)
sl.append(15)
sl.delete(1)  
sl.traverse()
               
        