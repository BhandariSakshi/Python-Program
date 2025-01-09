class Matrix:

    def Accept(self, Row, Col):

        Arr = []
        for i in range(0, Row):
            row = []
            for j in range(0, Col):
                element = int(input())
                row.append(element)
            Arr.append(row)

        return Arr

    def Display(self, Arr, Row, Col):

        for i in  range(0, Row):
            for j in range(0, Col):
                print(Arr[i][j],end=" ")
            print()

    def Minimum(self, Arr, Row, Col):

        iMin = Arr[0][0]
        for i in  range(0, Row):
            for j in range(0, Col):
                if iMin > Arr[i][j]:
                    iMin = Arr[i][j]

        return iMin

iRow = int(input("Enter the number of rows: "))
iCol = int(input("Enter the number of columns: "))

obj = Matrix()
Arr = obj.Accept(iRow, iCol)
obj.Display(Arr, iRow, iCol)
iRet = obj.Minimum(Arr,iRow, iCol)
print("Minimum element in the matrix is: ",iRet)