class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Linkedlist:
    def __int__(self,data):
        n=node(data)
        self.head=n

    def search(self,data):
        last=self.head
        prev = None
        found =False
        while last.next:
            if last.data==data:
                break
            prev=last
            last=last.next

            if found==False and key!=None:
                raise KeyError("%s not found")
            return (prev,last)

    def add_at_Start(self,data):
        NewNode = node(data)
        NewNode.next = self.head
        self.head = NewNode

    def add_at_End():
        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
            return

        last = self.head

        while(last.next):
            last = last.next
        last.next=NewNode

    def add_In_Between(self,middle_node,data):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = node(data)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

list = Linkedlist()
list.head = node("Mon")
e2 = node("Tue")
e3 = node("Thu")

list.head.next = e2
e2.next = e3

list.add_In_Between(list.head.next,"Fri")

list.listprint()