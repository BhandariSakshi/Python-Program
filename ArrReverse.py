class ArrayX:

    def Accept(self, Arr, iCount):

        print("Enter the elements: ")
        for i in range(0,iCount):
            A = int(input())
            Arr.append(A)

    def Reverse(self, Arr):

        print("Reversed array: ")
        for i in range(len(Arr)-1,-1,-1):
            print(Arr[i],end=" ")

def main():

    Arr = [] 
    iCount = 0
    iCount = int(input("Enter the number of elements that you want to store: "))

    obj = ArrayX()
    obj.Accept(Arr,iCount)
    obj.Reverse(Arr)

if __name__ == "__main__":
    main()