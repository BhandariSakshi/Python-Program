class Num:

    def Swap(self, iValue):

        temp = iValue[0]
        iValue[0] = iValue[1]
        iValue[1] = temp

def main():

    A = int(input("Enter the value of A: "))
    B = int(input("Enter the value of B: "))

    iValues = [A,B]

    obj = Num()
    obj.Swap(iValues)

    A = iValues[0]
    B = iValues[1]

    print("Value of A after swapping: ",A)
    print("Value of B after swapping: ",B)

if __name__ == "__main__":
    main()