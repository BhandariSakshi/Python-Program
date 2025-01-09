def CountDigit(iNo, iCount = 0):

    if iNo > 0:
        iNo = iNo // 10
        iCount += 1
        return CountDigit(iNo, iCount)

    return iCount

def main():

    iValue = int(input("Enter the number: "))

    iRet = CountDigit(iValue)
    print("Number of digit: ",iRet)

if __name__ == "__main__":
    main()