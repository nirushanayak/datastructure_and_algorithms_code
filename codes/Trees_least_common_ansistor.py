class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def TreeConstruction(data,n):
    Queue=[]
    if data[0]!=-1:
        head = Node(data[0])
        Queue.append(head)
    i=1
    while i<n and Queue:
        prevNode= Queue.pop(0)
        #left
        if data[i] !=-1:
            currNode = Node(data[i])
            prevNode.left = currNode
            Queue.append(currNode)
        i = i+1
        if( i >= n):
            break
        if data[i] != -1:
            currNode = Node(data[i])
            prevNode.right = currNode
            Queue.append(currNode)
        i = i+1
    return head

def LCA( A, B, C):
       if (A == None):
           return -1
       if (A.val == B | A.val == C):
           return A.val
       left_node = LCA( A.left, B, C)
       right_node = LCA( A.right, B, C)
       if (left_node == -1 and right_node == -1):
           return -1
       print(left_node if left_node != -1 else right_node)
       return left_node if left_node != -1 else right_node


data=[73,15,20,34,35,5,14,16,26,-1,25,23,-1,30,3,36,-1,-1,7,24,11,32,-1,-1,21,-1,-1,-1,29,4,9,-1,33,13,-1,-1,-1,-1,22,31,-1,27,19,1,-1,12,18,6,-1,-1,-1,2,-1,-1,-1,-1,10,-1,-1,-1,-1,8,-1,28,-1,-1,-1,-1,-1,17,-1,-1,-1,-1]
root=TreeConstruction(data,len(data))
print(LCA(root,33,5))


