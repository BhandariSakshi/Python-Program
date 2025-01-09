class EvenOdd:
    def __init__(self, iNo):
        self.iNo = iNo

    def is_evenOdd(self):
        return self.iNo % 2 == 0
    
iValue = int(input("Enter the number: "))

obj = EvenOdd(iValue)
sobj = obj.is_evenOdd()

if sobj:
    print("It is even number")
else:
    print("It is odd number")
