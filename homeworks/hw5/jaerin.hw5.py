class LinkedList():
    def __init__(self,value):
# Note that the function takes in an integer, not a Node
        if type(value)!=int:
            raise TypeError
# If not, let it return a type error
        else:
            self.list=[Node(value)]

    def length(self):
        return(len(self.list))

    def addNode(self,new_value):
# the function requires an integer as the input.
        if type(new_value)!=int:
            raise TypeError
# If there is nothing in the list, just add one.
        if len(self.list)==1:
            self.list.append(Node(new_value))
# If there is something at the end, add the value after it
        else:
            self.addNodeAfter(new_value,self.list[len(self.list)-1])

# An error is defined, for when an input Node is not found in the list.
    def InputError(error):
        """Can't find the input Node in the LinkedList."""
        pass

    def addNodeAfter(self,new_value,after_node):
        if type(new_value)!=int:
            raise TypeError
# after_node should be a Node
        if type(after_node)!=Node:
            raise TypeError
# after_node should be in the list
        if after_node not in self.list:
            raise InputError
# find where 'after_node' is
        loc=self.list.index(after_node)
        # Set new 'next'
        self.list[loc].next=new_value
        # if there was no element after 'after_node',
        if len(self.list)-1==loc:
        # just insert new_value without further modification
            self.list.insert(loc+1,Node(new_value))
        # if not, it should be .next for new_value.
        else:
            new_next=self.list[loc+1].value
            self.list.insert(loc+1,Node(new_value,new_next))

    def addNodeBefore(self,new_value,before_node):
    # Reverse what's done for addNodeAfter
        if type(new_value)!=int:
            raise TypeError
        if type(before_node)!=Node:
            raise TypeError
        if before_node not in self.list:
            raise InputError
        loc=self.list.index(before_node)
    # If there was an element before 'before_node',
        if loc>0:
    # list[loc-1].next should be modified
            self.list[loc-1].next=new_value
        # The rest goes the same for any list.
        new_next=self.list[loc].value
        self.list.insert(loc,Node(new_value,new_next))
        
    def removeNode(self,node_to_remove):
    # There should be the node to start with.
        if type(node_to_remove)!=Node:
            raise TypeError
        if node_to_remove not in self.list:
            raise InputError
    # Then, search where the node is
        loc=self.list.index(node_to_remove)
        # modify .next of the preceeding element
        if loc>0:
            if len(self.list)>loc+1:
                self.list[loc-1].next=self.list[loc+1].value
            else:
                self.list[loc-1].nest=None
        # Removing
        del self.list[loc]

    def removeNodesByValue(self,value):
    # The value should be an integer.
        if type(value)!=int:
            raise TypeError
        loc=[]
    # Look for Nodes in the list with the value
        for i,node in enumerate(self.list):
            if node.value==value:
                loc.append(i)
    # Remove node for each location
        copy=self.list[:]
        for i in loc:
            removeNode(copy[i])

    def reverse(self):
    # Reverse the values and make the list from scratch
        values=[i.value in self.list].reverse
        newlist=Node(values[0])
        for i in values[1:]:
            newlist.addNode(i)
        self.list=newlist

    def __str__(self):
        nodes=[i for i in self.list]
        values=[i.value for i in self.list]

        return "For Nodes\n"+str(nodes)+"\n, values are\n"+str(values)

class Node:
    def __init__(self, _value=None, _next=None):
# Node requires integer as input, and _value should not be None
        if type(_value)!=int:
            raise TypeError
# _next can be None, but if not, it should be an integer
        if type(_next)!=int:
            if _next!=None:
                raise TypeError
        self.value=_value
        self.next=_next
        def __str__(self):
            return(str(self.value))

