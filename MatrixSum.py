class Matrix:
    def Accept(self ,Row , Col):

        Arr = []
        
        print("Enter the matrix elements: ")
        for i in range(0,Row):
            row = []
            for j in range(0,Col):
                element = int(input())
                row.append(element)
            Arr.append(row)

        return Arr

    def Display(self,Arr, Row, Col):

        print("Matrix is: ")
        for i in range(0,Row):
            for j in range(0, Col):
                print(Arr[i][j],end=" ")
            print()

    def Summation(self,Arr, Row, Col):
        iSum = 0
        for i in range(0,Row):
            for j in range(0, Col):
                iSum = iSum + Arr[i][j]

        return iSum
    
iRow = int(input("Enter the number of rows: "))
iCol = int(input("Enter the number of columns: "))


obj = Matrix()
Arr = obj.Accept(iRow,iCol)
obj.Display(Arr, iRow, iCol)
iRet = obj.Summation(Arr,iRow,iCol)
print("Summation of matrix elements is: ", iRet)