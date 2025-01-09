class ArrayX:
    def __init__(self, iSize):
        self.iSize = iSize
        self.Arr = [0] * iSize

    def Accept(self):
        print("Enter the elements:")
        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def PairSum(self, iTarget):

        for i in range(len(self.Arr)):
            for j in range(i + 1, len(self.Arr)):
                if self.Arr[i] + self.Arr[j] == iTarget:
                    return [i, j]  
        return None  

def main():
    iCount = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX(iCount)
    obj.Accept()

    iTarget = int(input("Enter the target number: "))

    result = obj.PairSum(iTarget)

    if result is not None:
        print(f"Pair found at indices: {result[0]} and {result[1]}")
    else:
        print("No pair found that sums up to the target value")

if __name__ == "__main__":
    main()
