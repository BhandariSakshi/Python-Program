class Pattern:

    def Display(self, iRow, iCol):
        i = 0
        j = 0
        for i in range(1,iRow+1):
            for j in range(1,iCol+1):
                print(j,"\t",end=" ")

            print()

iValue1 = int(input("Enter the number of rows: "))
iValue2 = int(input("Enter the number of columns: "))
obj = Pattern()
obj.Display(iValue1, iValue2)