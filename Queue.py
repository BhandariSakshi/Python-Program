class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.First = None
        self.iCount = 0

    def Count(self):
        return self.iCount
    
    def Display(self):
        temp = self.First

        while temp != None:
            print(temp.data)
            temp = temp.next

        print()

    def EnQueue(self, data):
        newn = node(data)

        if self.First == None:
            self.First = newn

        else:
            temp = self.First

            while temp.next != None:
                temp = temp.next

            temp.next = newn

        self.iCount = self.iCount + 1

    def DeQueue(self):

        iValue = 0

        if self.First == None:
            print("Queue is empty")

        elif self.First.next == None:
            self.First = None

        else:
            iValue = self.First.data
            self.First = self.First.next

        self.iCount = self.iCount - 1

        return iValue


obj = Queue()

obj.EnQueue(11)
obj.EnQueue(21)
obj.EnQueue(51)
obj.EnQueue(101)

obj.Display()
iRet = obj.Count()
print("Number of elements: ",iRet)

iRemoved = obj.DeQueue()
print("Removed element is: ",iRemoved)

obj.Display()
iRet = obj.Count()
print("Number of elements: ",iRet)