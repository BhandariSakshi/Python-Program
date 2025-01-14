class MatrixX:

    def Accept(self, Row, Col):

        Arr = []

        for i in range(0, Row):
            row = []
            for j in range(0, Col):
                element = int(input())
                row.append(element)
            Arr.append(row)

        return Arr
    
    def Display(self,Arr, Row, Col):

        for i in range(0, Row):
            for j in range(0, Col):
                print(Arr[i][j],end=" ")
            print()

    
    def SumEvenOdd(self, Arr, Row, Col):

        iSumE = 0
        iSumO = 0
        for i in range(0, Row):
            for j in range(0, Col):
                if Arr[i][j] % 2 == 0:
                    iSumE = iSumE + Arr[i][j]
                else:
                    iSumO = iSumO + Arr[i][j]

        print("Sum of even element is: ",iSumE)
        print("Sum of odd element is: ",iSumO)
    
        


def main():

    iRow = int(input("Enter the number of rows: "))
    iCol = int(input("Enter the number of columns: "))

    obj = MatrixX()

    Arr = obj.Accept(iRow, iCol)
    obj.Display(Arr, iRow, iCol)
    obj.SumEvenOdd(Arr, iRow, iCol)


if __name__ == "__main__":
    main()