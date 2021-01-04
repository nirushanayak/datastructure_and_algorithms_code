class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        curr = self.head
        while(curr.next != None):
            curr=curr.next
        curr.next = Node(data)

    def print_list(self):
            curr = self.head
            while (curr != None):
                print(curr.data)
                curr = curr.next

def print_two_list(L1,L2):
    list1 = L1.head
    list2 = L2.head
    list1_len = list2_len =0
    while(list1!=None):
        list1_len = list1_len+1
        list1 = list1.next
    while (list2 != None):
        list2_len = list2_len + 1
        list2 = list2.next
    if list1_len>list2_len:
        diff= list1_len-list2_len
        intersection_data=find_intersection(L1.head,L2.head)
    else:
        diff = list2_len - list1_len
        intersection_data=find_intersection(L2.head, L1.head,diff)
    print(intersection_data)

def find_intersection(L1,L2,diff):
    count=0
    p1=L1
    p2=L2
    while(count!=diff):
        p1=p1.next
        count = count+1
    while(p1 and p2):
        if (p1.data == p2.data):
            return p1.data
        p1=p1.next
        p2=p2.next

    return None


list1 = LinkedList()
list1.head = Node(1)
list1.head.next = Node(2)
list1.head.next.next =e= Node(3)
node=e.next= Node(4)
e.next.next =  Node(5)
# list1.print_list()

list2= LinkedList()
list2.head= Node(10)
list2.head.next = Node(9)
list2.head.next.next =e3= Node(8)
e3.next= Node(7)
e3.next.next = enode =  Node(6)
enode.next = node
# list2.print_list()

print_two_list(list1,list2)

