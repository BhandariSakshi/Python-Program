class Factorial:
    def __init__(self, iNo):
        self.iNo = iNo

    def Find(self):
        iFact = 1
        for i in range(1, self.iNo+1):
            iFact = iFact * i

        return iFact
     



iValue = int(input("Enter the number: "))

obj = Factorial(iValue)

iRet = obj.Find()

print("factorial of",iValue," is: ",iRet)