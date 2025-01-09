class ArrayX:

    def Accept(self, Arr, iCount):

        i = 0
        print("Enter elements: ")

        for i in range(0, iCount):

            A = int(input())
            Arr.append(A)

    def DisplaySumDigit(self, Arr):

        i = 0
        for i in Arr:

            iRet = self.SumDigit(i)

            print(f"Sum of {i} is {iRet}")

    def SumDigit(self, iNo):

        iSum = 0

        while iNo != 0:
            iSum = iSum + (iNo % 10)
            iNo = iNo // 10

        return iSum


def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()
    obj.Accept(Arr, iCount)
    obj.DisplaySumDigit(Arr)

if __name__ == "__main__":
    main()