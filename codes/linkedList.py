class Node():
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp!= None:
            print(temp.data)  
            temp = temp.next

    def insertList(self, node, pos):
        position = pos
        count =0
        curr= None
        Next = self.head
        while(count !=position):
            count = count+1
            curr = Next
            Next = Next.next
        # print(curr.data)
        # print(Next.data)
        node.next = Next
        curr.next = node

list = LinkedList()
list.head = Node("1")
node2 = Node("2")
node3 = Node("3")
list.head.next = node2
node2.next = node3

node4 = Node("4")
list.insertList(node4, 1)

# node4 = Node("5")
# list.insertList(node4,5)
#
# node4 = Node("6")
# list.insertList(node4,6)
#
# node5 = Node("7")
# list.insertList(node5, 7)
list.printList()


