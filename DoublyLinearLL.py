class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def Display(First):
    temp = First
    print("<=>",end= " ")
    while temp:
        print("| ",str(temp.data)," |->",end=' ')
        temp = temp.next

    print("None")

def Count(First):
    temp = First
    iCnt = 0

    while temp:
        iCnt = iCnt+1
        temp = temp.next

    return iCnt
    

def InsertFirst(First, data):
    newn = node(data)

    if First == None:
        First = newn

    else:
        First.prev = newn
        newn.next = First
        First = newn

    return First

def InsertLast(First, data):
    newn = node(data)

    if First == None:
        First = newn

    else:
        temp = First

        while temp.next != None:
            temp = temp.next

        temp.next = newn
        newn.prev = temp

    return First

def InsertAtPos(First, data, iPos):
    newn = node(data)
    iLength = Count(First)

    if iPos < 1 and iPos > iLength+1:
        print("Invalid Position")

    if iPos == 1:
        InsertFirst(First)

    elif iPos == iLength+1:
        InsertLast(First)

    else:
        temp = First

        for i in range(1, iPos-1):
            temp = temp.next

        newn.prev = temp
        newn.next = temp.next
        temp.next = newn

        return First
    
def DeleteFirst(First):

    if First == None:
        print("Linked List is empty")

    elif First.next == None:
        First = None

    else:
        First = First.next

        return First
    
def DeleteLast(First):

    if First == None:
        print("Linked List is empty")

    elif First.next == None:
        First = None

    else:
        temp = First

        while temp.next.next != None:
            temp = temp.next

        temp.next = None

        return First
    
def DeleteAtPos(First, iPos):

    iLength = Count(First)

    if iPos < 1 and iPos > iLength:
        print("Invalid Position")

    if iPos == 1:
        DeleteFirst(First)

    elif iPos == iLength:
        DeleteLast(First)

    else:
        temp = First

        for i in range(1,iPos-1):
            temp = temp.next

        temp.next = temp.next.next

        return First
        
Head = None

Head = InsertFirst(Head,101)
Head = InsertFirst(Head,51)
Head = InsertFirst(Head,21)
Head = InsertFirst(Head,11)

Display(Head)

iRet = Count(Head)
print("Number of nodes: ",iRet)

Head = InsertLast(Head,111)
Head = InsertLast(Head,121)
Head = InsertLast(Head,151)

Display(Head)

iRet = Count(Head)
print("Number of nodes: ",iRet)

Head = InsertAtPos(Head,31, 3)

Display(Head)

iRet = Count(Head)
print("Number of nodes: ",iRet)

Head = DeleteFirst(Head)

Display(Head)

iRet = Count(Head)
print("Number of nodes: ",iRet)

Head = DeleteLast(Head)

Display(Head)

iRet = Count(Head)
print("Number of nodes: ",iRet)

Head = DeleteAtPos(Head, 3)

Display(Head)

iRet = Count(Head)
print("Number of nodes: ",iRet)