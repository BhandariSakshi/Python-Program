class Bitwise:

    def Xor(self, iNo1, iNo2):

        iResult = iNo1 ^ iNo2

        return iResult

def main():

    iValue1 = int(input("Enter the first number: "))

    iValue2 = int(input("Enter the second number: "))

    obj = Bitwise()

    iRet = obj.Xor(iValue1, iValue2)
    print("Bitwise Xor of number is: ", iRet)

if __name__ == "__main__":
    main()