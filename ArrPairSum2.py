class ArrayX:
    def __init__(self, iSize):
        self.iSize = iSize
        self.Arr = [0] * iSize

    def Accept(self):
        print("Enter the elements:")
        for i in range(self.iSize):
            self.Arr[i] = int(input())

    def PairSum(self, iTarget):

        Start = 0
        End = len(self.Arr)-1

        while Start < End:
            Pairsum = self.Arr[Start] +   self.Arr[End]

            if Pairsum > iTarget:
                End -= 1
            elif Pairsum < iTarget:
                Start += 1
            else:
                return [Start,End]
            
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
