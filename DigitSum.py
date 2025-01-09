class Digits:
    def __init__(self, iNo):
        self.iNo = iNo
    
    def DigitSum(self):
        iSum = 0
        while self.iNo != 0:
            iSum = iSum + (self.iNo%10)
            self.iNo = self.iNo // 10

        return iSum
    
iValue = int(input("Enter the number: "))

obj = Digits(iValue)

iRet = obj.DigitSum()

print("Sum of digits: ",iRet)