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

    def Maximum(self, Arr, Row, Col):

        iMax = Arr[0][0]
        for i in  range(0, Row):
            for j in range(0, Col):
                if iMax < Arr[i][j]:
                    iMax = Arr[i][j]

        return iMax

iRow = int(input("Enter the number of rows: "))
iCol = int(input("Enter the number of columns: "))

obj = Matrix()
Arr = obj.Accept(iRow, iCol)
obj.Display(Arr, iRow, iCol)
iRet = obj.Maximum(Arr,iRow, iCol)
print("Maximum element in the matrix is: ",iRet)