class ArrayX:

    def __init__(self, iNo):
        self.iSize = iNo
        self.Arr = [0]*iNo

    def Accept(self):

        print("Enter the elements: ")
        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def CountBits(self, x):
        Count = 0
        while x != 0:
            Count += (x & 1)
            x >>= 1
        return Count

    def Xor(self):
        result = 0
        for i in range(self.iSize):
            ans = self.CountBits(i + 1)
            result ^= (self.Arr[i] + ans)
        return result



def main():

    iCnt = int(input("Enter the number of elements you want to store in the array: "))

    obj = ArrayX(iCnt)

    obj = ArrayX(iCnt)
    obj.Accept()

    iRet = obj.Xor()
    print("Ans is:", iRet)


if __name__ == "__main__":
    main()