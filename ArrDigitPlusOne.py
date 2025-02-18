class Solution:

    def Accept(self, Arr, iCount):

        print("Enter the elements: ")
        for i in range(iCount):
            A = int(input())
            Arr.append(A)

    def PlusOne(self,Arr):

        Ret = []

        for i in range(len(Arr)-1,0,-1):
            if Arr[i] < 9:
                Arr[i] += 1
                return Arr
            Arr[i] = 0

        Ret[0] = 1
        for i in range(1,len(Arr)):
            Ret[i] = Arr[i-1]
        
        Arr = Ret
        return Arr

    def Display(self, Arr):
        print("After adding one: ")
        for i in range(len(Arr)):
            print(Arr[i],end=" ")

def main():

    Arr = []
    iCount = int(input("Enter the number of elements you want to store: "))

    obj = Solution()
    obj.Accept(Arr,iCount)
    obj.PlusOne(Arr)
    obj.Display(Arr)
    

if __name__ == "__main__":
    main()