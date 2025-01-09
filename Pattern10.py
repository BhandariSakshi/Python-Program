class Pattern:
    def __init__(self, iNo):
        self.iNo = iNo

    def Display(self):
        i = 0

        for i in range(1, self.iNo+1):
            print(i,end=" ")
            print("*", end=" ")
            print(i,end=" ")

iValue = int(input("Enter number: "))
obj = Pattern(iValue)
obj.Display()