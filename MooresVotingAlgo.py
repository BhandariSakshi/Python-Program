class ArrayX:

    def __init__(self, iSize):
        self.iSize = iSize
        self.Arr = [0]*iSize

    def Accept(self):
        print("Enter the elements: ")

        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def MajorityElement(self):
        Max = 0
        iFreq = 0

        for i in range(self.iSize):
            if iFreq == 0:
               Max = self.Arr[i]

            if Max == self.Arr[i]:
               iFreq += 1

            else:
               iFreq -= 1
               

        return Max

def main():

    Arr = []
    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX(iCount)
    obj.Accept()

    iRet = obj.MajorityElement()
    print("Majority element in the array is: ",iRet)

if __name__ == "__main__":
    main()