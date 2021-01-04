import sys
global maximum
maximum = -sys.maxsize-1

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def TreeConstruction(data,n):
    Queue=[]
    if data[0]!=None:
        head = Node(data[0])
        Queue.append(head)
    i=1
    while i<n and Queue:
        prevNode= Queue.pop(0)
        #left
        if data[i] is not None:
            currNode = Node(data[i])
            prevNode.left = currNode
            Queue.append(currNode)
        i = i+1
        if( i >= n):
            break
        if data[i] is not None:
            currNode = Node(data[i])
            prevNode.right = currNode
            Queue.append(currNode)
        i = i+1
    return head


def FindMax(parentNode, currNode, ValTillParent):
    if(currNode is None):
        return
    if(parentNode is None):
        currVal = 0
    else:
         currVal = parentNode.data - currNode.data
         if currVal + ValTillParent > currVal:
             currVal = currVal + ValTillParent
         global maximum
         maximum = max(currVal,maximum)
    FindMax(currNode, currNode.left, currVal)
    FindMax(currNode, currNode.right, currVal)

data=[8,5,10,1,2,2,13]
root = TreeConstruction(data,7)
FindMax(None,root,0)
print(maximum)

data=[5,2,1]
maximum = -sys.maxsize-1
root = TreeConstruction(data,3)
FindMax(None,root,0)
print(maximum)

data=[1,2,3,None,None,None,7]
maximum = -sys.maxsize-1
root = TreeConstruction(data,7)
FindMax(None,root,0)
print(maximum)
