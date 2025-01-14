class ArrayX:
    def __init__(self,iSize):
        self.iSize = iSize
        self.Arr = [0]*iSize

    def Accept(self):

        print("Enter elements: ")
        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def FindDuplicate(self):

        ArrSorted = sorted(self.Arr)

        for i in range(self.iSize):
            if ArrSorted[i] == ArrSorted[i+1]:
                return ArrSorted[i]
            
        return -1



def main():

    Arr = []

    iLength = int(input("Enter the number of elements you want to store: "))
    obj = ArrayX(iLength)
    obj.Accept()
    iRet = obj.FindDuplicate()

    if iRet == -1:
        print("There is no duplicate element")
    else:
        print("Dupliacte element: ",iRet)

if __name__ == "__main__":
    main()