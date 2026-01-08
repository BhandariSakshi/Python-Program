class ArrayX:
    def __init__(self, iSize):
        self.iSize = iSize
        self.Arr = [0]*iSize
    
    def Accept(self):

        print("Enter the elements: ")
        for i in range(0,self.iSize):
            self.Arr[i] = int(input())

    def Display(self):

        newArr = [0]*self.iSize
        newSize = 0

        for i in range(0, self.iSize):
            iCnt = 0
            for j in range(0,i):
                if self.Arr[i] == self.Arr[j]:
                    iCnt += 1
                
            if iCnt == 0:
                newArr[newSize] = self.Arr[i]
                newSize += 1

        for i in range(0, newSize):
            iFreq = 0
            for j in range(0,self.iSize):
                if newArr[i] == self.Arr[j]:
                    iFreq += 1
                
            print(newArr[i], " occurs ",iFreq, " times ")

def main():
    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX(iCount)

    obj.Accept()
    obj.Display()


if __name__ == "__main__":
    main()