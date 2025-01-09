class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SCLL:
    def __init__(self):
        self.First = None
        self.Last = None
        self.iCount = 0

    def Count(self):
        return self.iCount
    
    def Display(self):
        temp = self.First
        if self.First == None and self.Last == None:
            print("Linked List is empty")
            return

        else:
            while True:
                print("| ",str(temp.data)," |->", end=" ")
                temp = temp.next

                if temp == self.First:
                    break

            print()

    def InsertFirst(self, data):

        newn = node(data)
        if self.First == None and self.Last == None:
            self.First = newn
            self.Last = newn

        else:
            newn.next = self.First
            self.First = newn

        self.Last.next = self.First

        self.iCount = self.iCount + 1

    def InsertLast(self,data):

        newn = node(data)

        if self.First == None and self.Last == None:
            self.First = newn
            self.Last = newn

        else:
            self.Last.next = newn
            self.Last = newn

        self.Last.next = self.First

        self.iCount = self.iCount + 1

    def InsertAtPos(self, data, iPos):

        if iPos < 1 or iPos > self.iCount+1:
            print("Invalid Position")

        if iPos == 1:
            self.InsertFirst(data)

        elif iPos == self.iCount+1:
            self.InsertLast(data)

        else:
            newn = node(data)
            temp = self.First

            for i in range(1, iPos-1):
                temp = temp.next

            newn.next = temp.next.next
            temp.next = newn

            self.iCount = self.iCount + 1

    
    def DeleteFirst(self):

        if self.First == None or self.Last == None:
            print("Link List is empty")
            return
        
        elif self.First == self.Last:
            self.First = None
            self.Last = None

        else:
            self.First = self.First.next
            self.Last.next = self.First

        self.iCount = self.iCount - 1


    def DeleteLast(self):
        if self.First == None or self.Last == None:
            print("Link List is empty")
            return
        
        elif self.First == self.Last:
            self.First = None
            self.Last = None

        else:
            temp = self.First

            while temp.next != self.Last:
                temp = temp.next

            self.Last = temp
            self.Last.next = self.First

        self.iCount = self.iCount - 1

    def DeleteAtPos(self, iPos):

        if iPos < 1 or iPos > self.iCount:
            print("Link List is empty")

        if iPos == 1:
            self.DeleteFirst()

        elif iPos == self.iCount:
            self.DeleteLast

        else:
            temp = self.First

            for i in range(1, iPos-1):
                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount - 1


obj = SCLL()

obj.InsertFirst(101)
obj.InsertFirst(51)
obj.InsertFirst(21)
obj.InsertFirst(11)

obj.Display()

iRet = obj.Count()
print("Number of nodes: ",iRet)
        
obj.InsertLast(111)
obj.InsertLast(121)
obj.InsertLast(151)

obj.Display()

iRet = obj.Count()
print("Number of nodes: ",iRet) 

obj.InsertAtPos(31, 3)

obj.Display()

iRet = obj.Count()
print("Number of nodes: ",iRet) 

obj.DeleteFirst()

obj.Display()

iRet = obj.Count()
print("Number of nodes: ",iRet) 

obj.DeleteLast()

obj.Display()

iRet = obj.Count()
print("Number of nodes: ",iRet) 

obj.DeleteAtPos(3)

obj.Display()

iRet = obj.Count()
print("Number of nodes: ",iRet) 