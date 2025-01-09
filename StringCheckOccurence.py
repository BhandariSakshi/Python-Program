class Strings:

    def CheckOccurrence(self, Arr):

        bFlag = False

        for i in Arr:
            if i == 'w' or i == 'W':
                bFlag = True
                break
        
        return bFlag


def main():

    Arr = input("Enter the string: ")

    obj = Strings()

    bRet = obj.CheckOccurrence(Arr)

    if bRet == True:
        print("Charecter is present")

    else:
        print("Charecter is not present")

if __name__ == "__main__":
    main()