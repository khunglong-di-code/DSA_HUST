"""
ADT Linked List structure 
"""

class Node:

    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.SSpointer = None # This Spointer will always point into first node

    def appendLast(self, data):
        Newnode = Node(data)
        if self.Spointer == None:
            self.Spointer = Newnode
            return
        else:
            Last = self.Spointer
            while (Last != None): 
                Last = Last.next
            Last.next = Newnode
            return
        
    def appendFirst(self, data):
        Newnode = Node(data)
        Newnode.next = self.Spointer
        self.Spointer = Newnode
        return

    def RemoveLast(self):
        if self.Spointer == None:
            return     
        elif self.Spointer.next == None:
            self.Spointer == None
        else:
            Last = self.Spointer
            while (Last.next.next is not None):
                Last = Last.next
            Last.next = None
    
    def RemoveFirst(self):
        if self.Spointer == None:
            return
        else:
            First = self.Spointer
            self.Spointer = self.Spointer.next
            del First

    def Linked_A_List (self, list):
        for i in list:
            self.appendLast(i)
        return
    
    def count (self):
        if self is None:
            return 0
        else:
            Count = self.Spointer
            Sum = 0
            while (Count is not None):
                Sum += 1
                Count = Count.next
            return Sum
    

class DNode (Node):
    def __init__ (self, data, next = None, prev = None):
        super().__init__()
        self.prev = prev
        
class DLinkedList:
    def __init__ (self):
        self.Dpointer = None

    def appendLast(self, data):
        NewDNode = DNode(data)
        if self.Dpointer is None:
            self.Dpointer = NewDNode
        else:
            Last = self.Dpointer
            while (Last.next is not None ):
                Last = Last.next
        Last.next = NewDNode
        NewDNode.prev = Last
            
    def appendFirst(self, data):
        NewDNode = DNode(data)
        if (self.Dpointer == None):
            self.Dpointer = NewDNode
        else:
            NewDNode.next = self.Dpointer
            (self.Dpointer).prev = NewDNode
            self.Dpointer = NewDNode 
    
    def RemoveLast(self):
        if (self.Dpointer).next = None:
            self.Dpointer = None
        else:
            Last = self.Dpointer
            while (Last.next is not None):
                Last = Last.next
            Last.prev.next = None
            del Last

    def RemoveFirst(self):
        if self.Dpointer is None:
            return
        
        else: 
            temp = self.Dpointer          
            self.Dpointer = self.Dpointer.next
            self.Dpointer.prev = None
            del temp
   
    def DLinked_A_List(self,list):
        for i in list:
            self.appendLast(i)

    def Count(self):
        if self is None:
            return 0
        else:
            Count = self.Spointer
            Sum = 0
            while (Count is not None):
                Sum += 1
                Count = Count.next
            return Sum