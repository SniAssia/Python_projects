class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None :
            return 0
        else :
            current = self.head
            while current :
                print(current.data , end=" => ")
                current = current.next
            print(0)
            print()
    def reverse(self):
        if self.head == None :
            return 0
        else:
            queue = []
            current = self.head
            while current :
                queue.append(current.data)
                current = current.next
            while queue :
                cur = queue.pop()
                print(cur,end=" => ")
    # add at the head
    def add_head(self,elem):
        elem1=Node(elem)
        if self.head == None :
            return
        else :
            elem1.next = self.head
            self.head = elem1
    # add at the tail
    def add_tail(self,elem):
        elem1=Node(elem)
        if self.head == None :
            return
        else :
            current = self.head
            while current :
                if current.next == None :
                    current.next = elem1
                    break
                current= current.next
    # add after a specific value
    def add_after(self,elem,value):
        elem1=Node(elem)
        if self.head == None:
            return
        else :
            current = self.head
            while current :
                if current.data == value :
                    elem1.next = current.next
                    current.next = elem1
                current = current.next
    # add before a specific value
    def add_before(self,elem,value):
        elem1=Node(elem)
        if self.head == None :
            return
        else :
            previous = None
            bool = False
            current = self.head
            while current :
                if current.data == value:
                    bool = True
                    break
                previous = current
                current = current.next
            if bool == True :
                elem1.next = current
                previous.next = elem1
    # delete at the head
    def delete_head(self):
        if self.head == None :
            return
        else :
            self.head = self.head.next
    # delete at the tail
    def delete_tail(self):
        if self.head == None :
            return
        else:
            current = self.head
            while current.next.next :
                current = current.next
            current.next = None

    # delete after an element
    def delete_after(self,value):
        if self.head == None :
            return
        else :
            current = self.head
            while current :
                if current.data == value :
                    current.next = current.next.next
                    break
                current = current.next
    # delete before an element
    def delete_before(self,value):
        if self.head == None :
            return
        else :
            current=self.head
            prev1 = None
            prev2 = None
            bool = False
            while current.next:
                if current.data == value:
                    bool = True
                    break
                prev2 = current
                prev1= current.next
                current=current.next.next
            if bool == True:
                prev2.next = prev1.next
            else :
                print("there is no node with this value ")
    # split linked list into two linked lists
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def split1(self):
        l1 = LinkedList()
        l2 = LinkedList()
        if self.head is None:
            return
        else:
            current = self.head
            while current:
                if current.data % 2 == 0:
                    l1.append(current.data)
                else:
                    l2.append(current.data)
                current = current.next
        l1.display()
        l2.display()
    def merge(self,l1,l2):
        if l1.head == None :
            l2.display()
        elif l2.head == None :
            l1.display()
        else :
            cur1 = l1.head
            cur2 = l2.head
            while cur1 :
                while cur2 :
                    if cur1.data<cur2.data:
                        l2.add_before(cur1,cur2)
                    cur2 =cur2.next
                cur1 =cur1.next
        l2.display()

        
list = LinkedList()
list2 = LinkedList()
list.head = Node(1)
list.head.next = Node(2)
list.head.next.next=Node(4)
list.head.next.next.next=Node(6)
list.head.next.next.next.next= Node(8)
list.head.next.next.next.next.next = Node(10)

list2.head = Node(3)
list2.head.next = Node(5)
list2.head.next.next=Node(7)
list2.head.next.next.next=Node(9)
list2.head.next.next.next.next= Node(11)
list2.head.next.next.next.next.next = Node(12)

l.merge(list,list2)










