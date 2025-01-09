class ArrayX:

    def Accept(self, iCount, Arr):
        for i in range(0, iCount):
            A = int(input())
            Arr.append(A)

    def Minimum(self, Arr):
        iMin = Arr[0]

        for i in range(0, len(Arr)):
            if Arr[i] < iMin:
                iMin = Arr[i]

        return iMin
    
def main():

    Arr = []
    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()
    obj.Accept(iCount, Arr)
    iRet = obj.Minimum(Arr)
    print("Minimum element is: ",iRet)

    

if __name__ == "__main__":
    main()
