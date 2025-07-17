"""
ADT Node structure 
"""

class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.pointer = None # This pointer will always point into first node

    def appendLast(self, data):
        Newnode = Node(data)
        if self.pointer == None:
            self.pointer = Newnode
            return
        else:
            Last = self.pointer
            while (Last != None): 
                Last = Last.next
            Last.next = Newnode
            return
        
    def appendFirst(self, data):
        Newnode.next = self.pointer
        self.pointer = Newnode
        return

    def RemoveLast(self):
        if self.pointer == None:
            return
        else:
            Last = self.pointer
            while (Last.next.next is not None):
                Last = Last.next
            Last.next = None
    
    def RemoveFirst(self):
        if self.pointer == None:
            return
        else:
            First = self.pointer
            self.pointer = self.pointer.next
            del First
     