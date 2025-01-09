class number:

    def Find(self, iNo, iPow):

        iMul = 1

        for i in range(1, iPow+1):
            iMul = iMul*iNo

        return iMul
    
def main():

    iValue = int(input("Enter the number: "))
    iPower = int(input("Enter the value of power: "))

    obj = number()
    iRet = obj.Find(iValue, iPower)

    print("Value is: ",iRet)

if __name__ == "__main__":
    main()