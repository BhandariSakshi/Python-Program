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
    
    def DiagonalSum(self, Arr, Row, Col):

        iSum = 0
        for i in range(0, Row):
            for j in range(0, Col):
                if i == j:
                    iSum = iSum + Arr[i][j]

        print(f"Sum of diagonal is {iSum}")

            


iRow = int(input("Enter the number of row: "))
iCol = int(input("Enter the number of columns: "))

obj = Matrix()
Arr = obj.Accept(iRow, iCol)
obj.Display(Arr, iRow, iCol)
obj.DiagonalSum(Arr, iRow, iCol)