class ArrayX:

    def Accept(self, Arr, iCount):
        i = 0

        print("Enter elements: ")
        for i in range(0, iCount):

            A = int(input())
            Arr.append(A)

    def Average(self, Arr):
        i = 0
        Sum = 0

        for i in range(0, len(Arr)):
            Sum = Sum + Arr[i]

        return (float(Sum)/float(len(Arr)))


def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()
    obj.Accept(Arr, iCount)

    Ret = obj.Average(Arr)
    print("Value is: ",Ret)

if __name__ == "__main__":
    main()