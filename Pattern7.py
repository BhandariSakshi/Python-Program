class Pattern:
    def __init__(self,iNo):
        self.iNo = iNo

    def Display(self):
        i = 0
        for i in range(1, self.iNo+1):
            print("&",end= "\t")
        print("\n")

        for i in range(1, self.iNo+1):
            print("#",end= "\t")
        print("\n")

        for i in range(1, self.iNo+1):
            print("*",end= "\t")
        print("\n")


iValue = int(input("Enter the number: "))

obj = Pattern(iValue)
obj.Display()