class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.First = None
        self.iCount = 0

    def Count(self):
        return self.iCount
    
    def Display(self):
        temp = self.First
        print("Elements in the stack are: ")

        while temp != None:
            print(temp.data,end="\t")
            temp = temp.next

        print()

    def Push(self, data):
        newn = node(data)

        if self.First == None:
            self.First = newn

        else:
            newn.next = self.First
            self.First = newn

        self.iCount = self.iCount + 1

    def Pop(self):

        iValue = 0

        iValue = self.First.data
        self.First = self.First.next

        self.iCount = self.iCount - 1

        return iValue

obj = Stack()

obj.Push(11)
obj.Push(21)
obj.Push(51)
obj.Push(101)

obj.Display()

iRet = obj.Count()
print("Number of elements are: ", iRet)

iPop = obj.Pop()
print("Poped element is: ", iPop)

obj.Display()

iRet = obj.Count()
print("Number of elements are: ", iRet)