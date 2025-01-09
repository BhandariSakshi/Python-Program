class ArrayX:

    def Accept(self, iCount, Arr):

        print("Enter the elements: ")
        for i in range(0, iCount):
            A = int(input())
            Arr.append(A)

    def Update(self, Arr):

        for i in range(0, len(Arr)):
            Arr[i] += 1

    def Display(self, Arr):

        print("Array AFter updation: ")
        for i in range(0, len(Arr)):

            print(Arr[i])

    
def main():

    Arr = []

    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX()
    obj.Accept(iCount, Arr)
    obj.Update(Arr)
    obj.Display(Arr)

if __name__ == "__main__":

    main()