class CheckPrime:
    def __init__(self, iNo):
        self.iNo = iNo

    def Check(self):
        bFlag = True
        for i in range(2, self.iNo):
            if self.iNo % i == 0:
                bFlag = False
                break

        return bFlag

        
iValue = int(input("Enter the number: "))

obj = CheckPrime(iValue)

if obj.Check() == True:
    print("It is a prime number")
else:
    print("It is not a prime number")