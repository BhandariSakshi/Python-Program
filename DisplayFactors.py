class Display:

    def __init__(self, iNo):
        self.iNo = iNo

    def Factors(self):
        for i in range(1, self.iNo):
            if self.iNo % i == 0:
                print(i)

iValue = int(input("Enter the number: "))

obj = Display(iValue)

obj.Factors()