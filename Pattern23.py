class Pattern:
    def __init__(self, iNo):
        self.iNo = iNo

    def Display(self):
        i = 0
        ch = 'A'

        for i in range(1, self.iNo+1):
            print(ch,"\t", i, "\t", end=" ")
            ch = chr(ord(ch) + 1)

iValue = int(input("Enter the number: "))
obj = Pattern(iValue)
obj.Display()