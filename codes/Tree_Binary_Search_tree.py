import sys
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def isBst(root,min=-sys.maxsize-1,max=sys.maxsize):
    if root is None:
        return True
    if max < root.data > min:
        return False
    return isBst(root.left,min,root.data) and isBst(root.right,root.data,max)


def constructTree(treeList):
    i = 1
    Queue = []
    if treeList[0] is not None:
        head = Node(treeList[0])
        Queue.append((head))

    while i < len(treeList) and Queue:
        parent = Queue.pop(0)
        if treeList[i] is not None:
            currNode = Node(treeList[i])
            parent.left = currNode
            Queue.append(currNode)
        i = i+1
        if(i >= len(treeList)):
            break
        if treeList[i] is not None:
            currNode = Node(treeList[i])
            parent.right = currNode
            Queue.append(currNode)
        i = i + 1
    return head

def ConvertBTtoDLL(root):
    if root is None:
        return None,None
    root.left = ConvertBTtoDLL(root.left)[1]
    root.right = ConvertBTtoDLL(root.right)[0]
    if root.left is not None:
        root.left.right = root
    if root.right is not None:
        root.right.left = root
    return FindHeadAndTail(root)


def FindHeadAndTail(root):
    head=tail=root
    while(head.left != None):
        head=head.left
    while(tail.right !=None):
        tail=tail.right
    return [head,tail]


if __name__ == '__main__':
    data = [4, 4, 10, 5, 10, 7, 2, None, 3, 8,]
    root = constructTree(data)
    LinkedList = ConvertBTtoDLL(root)[0]
    # while(LinkedList.left is not None):
    #     LinkedList = LinkedList.left
    while(LinkedList is not None):
        print(LinkedList.data)
        LinkedList = LinkedList.right

    print(LinkedList.data)
    print(LinkedList)
    if (isBst(root)):
        print("Is BST")
    else:
        print("Not a BST")

