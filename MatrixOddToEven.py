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

    
    def OddToEven(self, Arr, Row, Col):

        
        for i in range(0, Row):
            for j in range(0, Col):
                if Arr[i][j] % 2 == 1:
                    Arr[i][j] += 1

def main():

    iRow = int(input("Enter the number of rows: "))
    iCol = int(input("Enter the number of columns: "))

    obj = MatrixX()

    Arr = obj.Accept(iRow, iCol)
    obj.Display(Arr, iRow, iCol)
    obj.OddToEven(Arr, iRow, iCol)
    obj.Display(Arr,iRow,iCol)


if __name__ == "__main__":
    main()