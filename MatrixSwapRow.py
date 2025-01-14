class MatrixX:

    def Accept(self, Row, Col):

        print("Enter the elements: ")

        Arr = []
        for i in range(0, Row):
            row = []
            for j in range(0, Col):
                element = int(input())
                row.append(element)
            Arr.append(row)
        
        return Arr
    
    def Display(self, Arr, Row, Col):

        print("Matrix is: ")

        for i in range(0, Row):
            for j in range(0, Col):
                print(Arr[i][j], end=" ")

            print()

    def SwapRow(self, Arr, Row, Col):

        temp = 0
        for i in range(0, Row-1):
            for j in range(0, Col):
                temp = Arr[i][j]
                Arr[i][j] = Arr[i+1][j]
                Arr[i+1][j] = temp
                
        


def main():

    iRow = int(input("Enter the number of rows: "))
    iCol = int(input("Enter the number of columns: "))

    obj = MatrixX()
    Arr = obj.Accept(iRow, iCol)
    obj.Display(Arr, iRow, iCol)
    obj.SwapRow(Arr, iRow, iCol)
    obj.Display(Arr,iRow, iCol)

if __name__ == "__main__":
    main()