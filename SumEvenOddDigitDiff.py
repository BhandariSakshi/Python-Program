class Digits:

    def Difference(self, iNo):

        iAns = 0
        iSumE = 0
        iSumO = 0

        while iNo > 0:

            iDigit = iNo % 10

            if iDigit % 2 == 0:
                iSumE += iDigit
            else:
                iSumO += iDigit

            iNo = iNo // 10

        iAns = iSumE - iSumO

        return iAns


def main():

    iValue = int(input("Enter the number: "))

    obj = Digits()

    iRet = obj.Difference(iValue)
    print("Difference between even and odd digit: ", iRet)

if __name__ == "__main__":
    main()