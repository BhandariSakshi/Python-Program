class Pattern:

    def Display(self, iRow, iCol):
        i = 0
        j = 0
        for i in range(0,iRow):
            for j in range(0,iCol):
                print("*\t",end=" ")

            print()

iValue1 = int(input("Enter the number of rows: "))
iValue2 = int(input("Enter the number of columns: "))
obj = Pattern()
obj.Display(iValue1, iValue2)