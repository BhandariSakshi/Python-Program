import math

class ArrayX:

    def Accept(self, Arr, iCount):
        i = 0

        print("Enter elements: ")
        for i in range(0, iCount):
            A = int(input())
            Arr.append(A)

    def MaxSum(self, Arr):
        iMax = Arr[0]
        CurrSum = 0

        for Start in Arr:
                CurrSum += Start

                iMax = max(CurrSum, iMax)

                if CurrSum < 0:
                     CurrSum = 0

        return iMax


def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()

    obj.Accept(Arr, iCount)

    iRet = obj.MaxSum(Arr)
    print("Maximum sum of subarray is: ", iRet)
    

if __name__ == "__main__":
    main()