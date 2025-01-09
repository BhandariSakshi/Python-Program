class CountFactors:
    def __init__(self, iNo):
        self.iNo = iNo
    
    def Count(self):
        iCount = 0
        for i in range(1, self.iNo):
            if self.iNo % i == 0:
                iCount = iCount + 1
        return iCount



iValue = int(input("Enter the number: "))

obj = CountFactors(iValue)

iRet = obj.Count()

print("Number of factors are: ",iRet)