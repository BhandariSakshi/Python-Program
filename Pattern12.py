class Pattern:
    def __init__(self, iNo):
        self.iNo = iNo

    def Display(self):
        
        for i in range(self.iNo, 0, -1):
            print(i,end=" ")
            

iValue = int(input("Enter the number: "))
obj = Pattern(iValue)
obj.Display()