class OddDigit:
    def __init__(self, iNo):
        self.iNo = iNo

    def Display(self):
        iDigit = 0
        while self.iNo > 0:
            iDigit = self.iNo % 10
            if iDigit % 2 != 0:
                print(iDigit)
            self.iNo = self.iNo // 10


iValue = int(input("Enter the number: "))

obj = OddDigit(iValue)

obj.Display()