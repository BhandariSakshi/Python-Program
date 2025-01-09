class Digit:
    def __init__(self, iNo):
        self.iNo = iNo

    def Reverse(self):
        iDigit = 0
        iRev = 0
        while self.iNo != 0:
            iDigit = self.iNo % 10
            iRev = (iRev*10) + iDigit
            self.iNo = self.iNo // 10

        return iRev


iValue = int(input("Enter the number: "))

obj = Digit(iValue)

iRet = obj.Reverse()
print(iRet)
