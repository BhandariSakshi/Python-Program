class Pattern:

    def Display(self, iRow, iCol):
        i = 0
        j = 0

        if iRow != iCol:
            print("Number of rows and columns should be equal")
            return 

        for i in range(1,iRow+1):
            for j in range(1,iCol+1):
                if i > j:
                    print("#\t", end=" ")
                elif i == j:
                    print("&\t",end=" ")
                else:
                    print("@\t", end=" ")

            print()

iValue1 = int(input("Enter the number of rows: "))
iValue2 = int(input("Enter the number of columns: "))
obj = Pattern()
obj.Display(iValue1, iValue2)