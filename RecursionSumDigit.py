def SumDigit(iNo, iSum = 0):

    if iNo > 0:
        iSum = iSum + (iNo%10)
        iNo = iNo // 10
        return SumDigit(iNo, iSum)

    return iSum

def main():

    iValue = int(input("Enter the number: "))

    iRet = SumDigit(iValue)
    print("Sum of digit: ",iRet)

if __name__ == "__main__":
    main()