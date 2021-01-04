# import re
# def solve( A):
#     A=A.strip(' ')
#     L=re.findall(r'\w+', A)
#     L_r = L[::-1]
#     print(" ".join(L_r))
#
# solve("    adf b      cdff d   ")


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

Q=[]

def K_smallest_elem(root,num):
    if root==None:
        return
    K_smallest_elem(root.left,num)
    if len(Q)>=num:
        return Q[-1]
    Q.append(root.data)
    K_smallest_elem(root.right,num)
    return Q[-1]

# data1=[12,8,13,2,10,None,None,1,3]
# data=[2,1,3]
# root = TreeConstruction(data,len(data))
#
# print(K_smallest_elem(root,2))
# print(Q)

def solve( A, B):
        if A == None and B == None:
            return
        if A and B:
            A.data = A.data + B.data
        elif B:
            return "B"
        res = solve(A.left if A else None, B.left if B else None)
        if res == "B":
            A.left = B.left
        res1 = solve(A.right if A else None, B.right if B else None)
        if res1 == "B":
            A.right = B.right
        return A


data1=[26, 5, 32]
root1=TreeConstruction(data1,len(data1))
data2=[87 ,80 ,97, 66 ,83, 90 ,98, 54 ,70, 81, 86]
root2=TreeConstruction(data2,len(data2))
root=solve(root1,root2)
print(root)
