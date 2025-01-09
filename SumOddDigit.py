
def Sum(iNo):
        iSum = 0
        iDigit = 0
        while iNo != 0:
            iDigit = iNo % 10
            if iDigit % 2 != 0:
                iSum = iSum + iDigit
            iNo = iNo // 10

        return iSum


iValue = int(input("Enter the number: "))

iRet = Sum(iValue)

print("Sum of odd numbers: ",iRet)