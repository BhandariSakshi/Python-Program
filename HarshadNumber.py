def HarshadNumber(iNum):

    oriNum = iNum
    iSum = 0
    while iNum > 0:
        iDigit = iNum % 10
        iSum = iSum + iDigit
        iNum = iNum // 10

    if oriNum % iSum == 0:
        print("Harshad Number")

    else:
        print("Not a Harshad Number")

def main():

    Num = int(input("Enter the number: "))

    HarshadNumber(Num)

if __name__ == "__main__":
    main()