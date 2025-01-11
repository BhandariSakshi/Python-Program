class Matrix:

    def Accept(self, Row, Col):

        Arr = []
        print("Enter the elements: ")
        for i in range(0, Row):
            row = []
            for j in range(0, Col):
                element = int(input())
                row.append(element)
            Arr.append(row)

        return Arr
    
    def Display(self,Arr, Row, Col):

        print("Matrix is: ")
        for i in range(0, Row):
            for j in range(0, Col):
                print(Arr[i][j], end=" ")
            
            print()
    
    def RowSum(self, Arr, Row, Col):

        
        for i in range(0, Row):
            iSum = 0
            for j in range(0, Col):
                iSum = iSum + Arr[i][j]

            print(f"Sum of row {i} is {iSum}")

            


iRow = int(input("Enter the number of row: "))
iCol = int(input("Enter the number of columns: "))

obj = Matrix()
Arr = obj.Accept(iRow, iCol)
obj.Display(Arr, iRow, iCol)
obj.RowSum(Arr, iRow, iCol)