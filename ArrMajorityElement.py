class ArrayX:

    def __init__(self, iSize):
        self.iSize = iSize
        self.Arr = [0]*iSize

    def Accept(self):
        print("Enter the elements: ")

        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def MajorityElement(self):
        Max = -1

        for i in range(self.iSize):
            iFreq = 0
            for j in range(self.iSize):
                if self.Arr[i] == self.Arr[j]:
                    iFreq += 1
            
            if iFreq > self.iSize/2:
                Max = self.Arr[i]

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