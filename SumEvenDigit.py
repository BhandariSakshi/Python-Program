class Digit:
    def __init__(self, iNo):
        self.iNo = iNo

    def Sum(self):
        iSum = 0
        iDigit = 0
        while self.iNo != 0:
            iDigit = self.iNo % 10
            if iDigit % 2 == 0:
                iSum = iSum + iDigit
            self.iNo = self.iNo // 10

        return iSum


iValue = int(input("Enter the number: "))

obj = Digit(iValue)

iRet = obj.Sum()

print("Sum of even numbers: ",iRet)