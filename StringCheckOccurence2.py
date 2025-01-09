class Strings:

    def CheckOccurrence(self, Arr, ch):

        bFlag = False

        for i in Arr:
            if i == ch:
                bFlag = True
                break
        
        return bFlag


def main():

    Arr = input("Enter the string: ")

    #print("Enter a character: ", end="")
    #ch = sys.stdin.read(1) 
    
    cValue = input("Enter the charecter you want to search: ")[0]

    obj = Strings()

    bRet = obj.CheckOccurrence(Arr, cValue)

    if bRet == True:
        print("Charecter is present")

    else:
        print("Charecter is not present")

if __name__ == "__main__":
    main()