class Number:

    def CountOne(self, iNo):

        iDigit = 0
        iCount = 0
        while iNo != 0:

            iDigit = iNo % 2
            if iDigit == 1:
                iCount = iCount + 1
            iNo = iNo // 2

        return iCount

def main():

    iValue = int(input("Enter the number: "))

    obj = Number()
    iRet = obj.CountOne(iValue)
    print("Number of ones are: ",iRet)

if __name__ == "__main__":
    main()