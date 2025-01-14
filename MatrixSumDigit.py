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

    def SumDigit(self, Arr, Row, Col):

        iDigit = 0
        iSum = 0
        iNo = 0

        print("Matrix after sum: ")
        for i in range(0,Row):
            for j in range(0, Col):
                iNo = Arr[i][j]
                while iNo != 0:
                    iDigit = iNo % 10
                    iSum = iSum + iDigit
                    iNo = iNo // 10

                print(iSum, end=" ")
                iSum = 0
            
            print()


def main():

    iRow = int(input("Enter the number of rows: "))
    iCol = int(input("Enter the number of columns: "))

    obj = MatrixX()
    Arr = obj.Accept(iRow, iCol)
    obj.Display(Arr, iRow, iCol)
    obj.SumDigit(Arr, iRow, iCol)

if __name__ == "__main__":
    main()