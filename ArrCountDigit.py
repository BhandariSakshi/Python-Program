class ArrayX:

    def Accept(self, Arr, iCount):

        i = 0
        print("Enter elements: ")

        for i in range(0, iCount):

            A = int(input())
            Arr.append(A)

    def DisplayCountDigit(self, Arr):

        i = 0
        for i in Arr:

            iRet = self.CalculateDigit(i)

            print(i," contains ",iRet," digits")

    def CalculateDigit(self, iNo):

        iCount = 0

        while iNo != 0:
            iCount += 1
            iNo = iNo // 10

        return iCount


def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()
    obj.Accept(Arr, iCount)
    obj.DisplayCountDigit(Arr)

if __name__ == "__main__":
    main()