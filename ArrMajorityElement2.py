class ArrayX:

    def __init__(self, iSize):
        self.iSize = iSize
        self.Arr = [0]*iSize

    def Accept(self):
        print("Enter the elements: ")

        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def Sort(self):
        self.Arr.sort()

    def MajorityElement(self):
        Max = self.Arr[0]
        iFreq = 1

        for i in range(1,self.iSize):
            
            if self.Arr[i] == self.Arr[i-1]:
                iFreq += 1
            else:
                iFreq = 1
                Max = self.Arr[i]

            if iFreq > self.iSize/2:
                    return Max

        return Max

def main():

    Arr = []
    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX(iCount)
    obj.Accept()
    obj.Sort()

    iRet = obj.MajorityElement()
    print("Majority element in the array is: ",iRet)

if __name__ == "__main__":
    main()