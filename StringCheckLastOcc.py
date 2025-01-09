class Strings:

    def CheckLastOcc(self, Str, ch):

        iCount = 1
        iPos = -1

        for i in Str:
            if i == ch:
                iPos = iCount
            iCount += 1

        return iPos

def main():

    Arr = input("Enter the string: ")

    cValue = input("Enter the charecter: ")[0]

    obj = Strings()

    iRet = obj.CheckLastOcc(Arr, cValue)

    if iRet != -1:
        print("Last Occurrence of charecter is: ",iRet)

    else:
        print("There is no such charecter")

if __name__ == "__main__":
    main()