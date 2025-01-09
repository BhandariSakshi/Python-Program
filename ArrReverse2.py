class ArrayX:

    def Accept(self, Arr, iCount):
        i = 0
        print("Enter elements: ")

        for i in range(0, iCount):
            A = int(input())
            Arr.append(A)

    def Display(self, Arr):
        i = 0

        for i in range(0, len(Arr)):
            print(Arr[i],end=" ")

    def Reverse(self, Arr):
        iStart = 0
        iEnd = len(Arr) - 1
        temp = 0

        while iStart < iEnd:

            temp = Arr[iStart]
            Arr[iStart] = Arr[iEnd]
            Arr[iEnd] = temp

            iStart += 1
            iEnd -= 1

def main():

    iCount = int(input("Enter the number of elements you want to store: "))
    Arr = []

    obj = ArrayX()
    obj.Accept(Arr, iCount)
    print("Array before reversing: ")
    obj.Display(Arr)
    obj.Reverse(Arr)
    print("\nArray after reversing: ")
    obj.Display(Arr)


if __name__ == "__main__":
    main()