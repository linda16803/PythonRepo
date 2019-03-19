"""This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 16 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next=None
        

def getLen(linkedlist):
    if not linkedlist:
        return 0
    return getLen(linkedlist.next)+1

def getNode(A, B):
    lenA, lenB = getLen(A), getLen(B)
    iterA, iterB = A, B
    
    print(lenA)
    print(lenB)
    """LinkedList ignor difference part from beginning for longer list"""
    
    if lenA > lenB:
        for _ in range(lenA-lenB):
            iterA = iterA.next
    else:
        for _ in range(lenB-lenA):
            iterB = iterB.next
    
    """when length same, starting to comparing linked list one by one until match."""
    """after first node match,all rest linked list will be same"""
    
    while iterA != iterB:
        iterA =iterA.next
        iterB = iterB.next
        
    return iterA

node1=Node(3)
node2=Node(7)
node3=Node(8)
node4=Node(10)
node1.next=node2
node2.next=node3
node3.next=node4

nodeB1=Node(99)
nodeB2=Node(1)
nodeB3=Node(16)

nodeB1.next=nodeB2
nodeB2.next=nodeB3
nodeB3.next=node3
print(getNode(node1,nodeB1).val)