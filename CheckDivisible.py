class CheckDivisibility:

    def __init__(self, iNo):
        self.iNo = iNo

    def Check(self):
        if self.iNo % 3 == 0 and self.iNo % 5 == 0:
            return True
            
        
iValue = int(input("Enter number: "))

obj = CheckDivisibility(iValue)
bRet = obj.Check()

if bRet == True:
    print("It is divisible by 3 and 5")
else:
    print("It is not divisible by 3 and 5")