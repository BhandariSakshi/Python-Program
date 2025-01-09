class DisplayDigit:
    def __init__(self, iNo):
        self.iNo = iNo

    def Display(self):
        iDigit = 0
        while self.iNo > 0:
            iDigit = self.iNo % 10
            print(iDigit)
            self.iNo = self.iNo // 10


iValue = int(input("Enter the number: "))

obj = DisplayDigit(iValue)
obj.Display()