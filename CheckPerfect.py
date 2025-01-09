class CheckPerfect:
    def __init__(self, iNo):
        self.iNo = iNo

    def Check(self):
        iSum = 0
        for i in range(1, self.iNo):
            if self.iNo % i == 0:
                iSum = iSum + i

        if iSum == self.iNo:
            return True
        else:
            return False
        
iValue = int(input("Enter the number: "))

obj = CheckPerfect(iValue)

if obj.Check() == True:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
