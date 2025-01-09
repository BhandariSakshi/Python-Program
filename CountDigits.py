class DisplayDigit:
    def __init__(self, iNo):
        self.iNo = iNo

    def Count(self):
        iCnt = 0
        while self.iNo > 0:
            iCnt = iCnt + 1
            self.iNo = self.iNo // 10
        
        return iCnt


iValue = int(input("Enter the number: "))

obj = DisplayDigit(iValue)
iRet = obj.Count()
print("Number of digits are: ",iRet)