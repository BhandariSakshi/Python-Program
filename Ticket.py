class Ticket:

    def __init__(self, iAge):
        self.iAge = iAge
    
    def Amount(self):
        if self.iAge <= 5:
            return 0
        elif self.iAge > 5 and self.iAge <= 18:
            return 800
        elif self.iAge > 18 and self.iAge <= 60:
            return 1000
        else:
            return 500

iValue = int(input("Enter your age: "))

obj = Ticket(iValue)
iRet = obj.Amount()

print("Total amount is: ",iRet)


     



