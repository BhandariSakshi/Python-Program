class ArrayX:

    def Accept(self, Arr, iCount):

        print("Enter the elements: ")
        for i in range(0, iCount):
            A = int(input())
            Arr.append(A)

    def SingleNumber(self, Arr):

        iAns = 0
        for i in range(0, len(Arr)):
            iAns = iAns ^ Arr[i]

        return iAns

def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()

    obj.Accept(Arr, iCount)

    iRet = obj.SingleNumber(Arr)
    print("Single or unique number is: ",iRet)


if __name__ == "__main__":
    main()