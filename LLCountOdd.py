class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertFirst(Head, data):
    newn = node(data)
    if Head == None:
        Head = newn
    else:
        newn.next = Head
        Head = newn

    return newn

def InsertLast(Head, data):
    newn = node(data)
    if Head == None:
        Head = newn
    else:
        temp = Head
        while temp.next != None:
            temp = temp.next
        
        temp.next = newn

    return Head

def InsertAtPos(Head, data, iPos):
    newn = node(data)
    iLength = Count(Head)

    if iPos < 1 and iPos > iLength+1:
        print("Invalid Position")

    if iPos == 1:
        InsertFirst(Head)

    elif iPos == iLength+1:
        InsertLast(Head)

    else:
        temp = Head
        for i in range(1, iPos-1):
            temp = temp.next

        newn.next = temp.next
        temp.next = newn

    return Head

def DeleteFirst(Head):

    if Head == None:
        print("Linked List is empty")
        return Head

    else:
        Head = Head.next
        return Head
    
def DeleteLast(Head):

    if Head == None:
        print("Linked List is empty")
        return Head
    
    elif Head.next == None:
        Head = None

    else:
        temp = Head

        while temp.next.next != None:
            temp = temp.next

        temp.next = None
        return Head
    
def DeleteAtPos(Head, iPos):
    iLength = Count(Head)

    if iPos < 1 and iPos > iLength:
        print("Invalid Position")

    if iPos == 1:
        DeleteFirst(Head)

    elif iPos == iLength:
        DeleteLast(Head)

    else:
        temp = Head
        for i in range(1, iPos-1):
            temp = temp.next

        temp.next = temp.next.next

        return Head



def Display(Head):
    temp = Head
    while temp:
        print("| ",str(temp.data)," |->",end=' ')
        temp = temp.next

    print("None")

def Count(Head):
    temp = Head
    iCount = 0
    while temp:
        iCount = iCount + 1
        temp = temp.next

    return iCount

def CountOdd(Head):

    temp = Head
    iCnt = 0
    while temp:
        if temp.data % 2 != 0:
            iCnt += 1
        temp = temp.next

    return iCnt

Head = None
Head = InsertFirst(Head, 101)
Head = InsertFirst(Head, 51)
Head = InsertFirst(Head, 21)
Head = InsertFirst(Head, 11)

Display(Head)

iRet = Count(Head)
print("Number of nodes are: ",iRet)

Head = InsertLast(Head, 111)
Head = InsertLast(Head, 121)
Head = InsertLast(Head, 151)

Display(Head)

iRet = Count(Head)
print("Number of nodes are: ",iRet)

Head = InsertAtPos(Head, 31, 3)

Display(Head)

iRet = Count(Head)
print("Number of nodes are: ",iRet)

Head = DeleteFirst(Head)

Display(Head)

iRet = Count(Head)
print("Number of nodes are: ",iRet)

Head = DeleteLast(Head)

Display(Head)

iRet = Count(Head)
print("Number of nodes are: ",iRet)

Head = DeleteAtPos(Head, 3)

Display(Head)

iRet = Count(Head)
print("Number of nodes are: ",iRet)

iResult = CountOdd(Head)
print("Odd elements are: ",iResult)
    