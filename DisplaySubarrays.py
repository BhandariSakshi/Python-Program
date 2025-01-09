class ArrayX:

    def Accept(self, Arr, iCount):

        i = 0
        print("Enter elements: ")
        for i in range(0, iCount):
            A = int(input())
            Arr.append(A)

    def DisplaySubarray(self, Arr):

        for Start in range(0, len(Arr)):
            for End in range(Start, len(Arr)):
                for i in range(Start, End+1):
                    print(Arr[i],end=' ')

                print("\t")

            print("\n")

def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()

    obj.Accept(Arr, iCount)
    obj.DisplaySubarray(Arr)

if __name__ == "__main__":
    main()