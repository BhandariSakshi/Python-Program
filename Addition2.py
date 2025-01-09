class Addition:
    def __init__(self, iNo1, iNo2):
        self.iNo1 = iNo1
        self.iNo2 = iNo2

    def Add(self):
        iAns = self.iNo1 + self.iNo2
        print(iAns)


iValue1 = int(input("Enter the first number: "))
iValue2 = int(input("Enter the second number: "))

obj = Addition(iValue1, iValue2)

obj.Add()