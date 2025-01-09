class CheckPrime:
    def __init__(self, iNo):
        self.iNo = iNo

    def Check(self):
        iCount = 0
        for i in range(2, self.iNo):
            if self.iNo % i == 0:
                iCount = iCount + 1

        if iCount == 0:
            return True
        else:
            return False
        
iValue = int(input("Enter the number: "))

obj = CheckPrime(iValue)

if obj.Check() == True:
    print("It is a prime number")
else:
    print("It is not a prime number")