class CheckRange:
    def __init__(self, iNo):
        self.iNo = iNo

    def Check(self):
        if self.iNo >= 1 and self.iNo <= 10:
            return True

iValue = int(input("Enter the number: "))

obj = CheckRange(iValue)

bRet = obj.Check()

if bRet == True:
    print(f"{iValue} is in range")

else:
    print(f"{iValue} is not in range")

