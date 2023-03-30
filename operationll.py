class   Node:
    def __init__(self,value):
        self.value=value,
        self.next=None

class LinkList:
    def __init__(self,value):# constructor
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
     
    def print_list(self):# print list
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
                
    def append(self,value): #append method
        new_node=Node(value)
        
        if self.length ==0:# if the list is empty thennnn
            self.head=new_node
            self.tail=new_node
        else:                   # elseeee 
            self.tail.next=new_node
            self.tail=new_node    
        self.length+=1    
        return True   
    
   
    def pop(self):# pop method
        if self.length==0:
            return None
        
        temp=self.head   #logic
        pre=self.tail
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next= None
        self.length-=1    
       
        if self.length==0:  
            self.head=None
            self.tail=None   
        return temp.value    
              
    def prepend(self,value):      #push element
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):# popping the first elemnet of ll
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        
        if self.length==0:
            self.tail=None
        return temp      
       
    def get(self,index):# getting an elemnt at particular index
        if index<0 or index>self.length:
            None
        temp=self.head
        for _ in range(index):#_ is similar to i but we use i to print the variable 
            temp=temp.next
        return temp    # FOR PRINTING THE VALUE WE CAN RETURN TEMP.VALUE
    
    def set_value(self,index,value):# changing value at particular index
        temp=self.get(index)# here we are calling a method inside another method
        if temp:# is temp is not null thennnn we go inside temp
             temp.value=value
             return True
        return False
            
    def insert(self,index,value):# inserting a node at start or end or in middle
        if index<0 or index>self.length:
            return False
        
        if index==0:
            return self.prepend(value)
        
        if index==self.length:
            return self.append(value)
        
        new_node=Node(value)
        temp=self.get(index-1)# the node that is before the index where we want to enter our new node
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True 
                         
    def remove(self,index):
        if index<0 or index>self.length:
            return None
        
        if index==0:
            return self.pop_first()
        
        if index==self.length-1:# removing the last item
            return self.pop()
        
        previous=self.get(index-1)
        temp=previous.next
        previous.next=temp.next
        temp.next=None# REMOVING THE NODE WE WANT TO REMOVE
        self.length-=1
        return temp
    
    def reverse(self):# common interview question
        temp=self.head
        self.head=self.tail
        self.tail=temp
        
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
            
        
            
        




mylinklist=LinkList(1)
mylinklist.append(2)
mylinklist.append(3)
mylinklist.pop()# no need to pass value the last node will be popped in pop operation
mylinklist.prepend(11)
mylinklist.pop_first()
mylinklist.append(3)
mylinklist.prepend(0)
print('at index two the element is',mylinklist.get(2))
mylinklist.set_value(1,44) 
mylinklist.insert(2,1)
mylinklist.remove(1)
mylinklist.print_list()
mylinklist.reverse()
print('\n')
print('after reversinng')
print('\n')
mylinklist.print_list()

