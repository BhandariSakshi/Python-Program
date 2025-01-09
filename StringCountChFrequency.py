class Strings:

    def CountFrequency(self, Arr , ch):
        iCount = 0

        for i in Arr:
            if i == ch:
                iCount += 1

        return iCount
        

def main():

    Arr = input("Enter the string: ")
    cValue = input("Enter the charecter: ")[0]

    obj = Strings()
    iRet = obj.CountFrequency(Arr, cValue)

    print("Number of times charecter occurs: ",iRet)

if __name__ == "__main__":
    main()