class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def n_node(self, pos):
        count = pos-1
        curr = None
        next1 = self.head
        prev = None
        while(count==pos-1):
            curr=next1
            next1,count = self.move_to_pos(next1, pos-1)
            # print(next1.data)
            if count==pos-1:
                prev = curr
        prev, count =  self.move_to_pos(prev, count)
        return prev.data

    def move_to_pos(self,curr, pos):
        count = 0
        while(count != pos):
            if(curr.next != None):
                curr = curr.next
                count = count+1
            else:
                return None,count
        return curr,count

    def add_node(self, data):
        curr = self.head
        while(curr.next != None):
            curr=curr.next
        curr.next = Node(data)


    def print_list(self):
        curr=self.head
        while(curr != None):
            print(curr.data)
            curr=curr.next

    def reverse_linked_list(self):
        prev=None
        curr=self.head
        next1=curr.next
        while(curr):
            curr.next = prev
            prev = curr
            curr = next1
            if next1:
                next1 = next1.next
        self.head = prev

    def middle_element(self):
        slow=fast=self.head
        while(fast.next  and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        return slow.data

    def reverse_consicutive_node(self,head):
        if head == None or head.next ==None:
            return head
        else:
            temp=head.next
            head.next=temp.next
            temp.next=head
            head=temp
            head.next.next= self.reverse_consicutive_node(head.next.next)
            return head




list=LinkedList()
list.head = Node(1)
list.add_node(2)
list.add_node(3)
list.add_node(4)
list.add_node(5)
list.add_node(6)
list.add_node(7)
list.add_node(8)
list.add_node(9)
list.add_node(10)
list.print_list()
list.print_list()
print("middle ele is %s",list.middle_element())
data=list.n_node(2)
print("n th node from list is : %s",data)
list.reverse_linked_list()
print("after reversing:\n")
reverse_list=list.reverse_consicutive_node(list.head)
list.head=reverse_list
print("after consecutive reversing :")
list.print_list()
