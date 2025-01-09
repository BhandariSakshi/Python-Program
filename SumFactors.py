class SumFactors:
    def __init__(self, iNo):
        self.iNo = iNo

    def Sum(self):
        iSum = 0
        for i in range(1, self.iNo):
            if self.iNo % i == 0:
                iSum = iSum + i

        return iSum



iValue = int(input("Enter the number: "))

obj = SumFactors(iValue)

iRet = obj.Sum()

print("Sum of Factors are: ",iRet)