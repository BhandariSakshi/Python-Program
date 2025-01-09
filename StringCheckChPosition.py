class Strings:

    def CheckPosition(self, Arr , ch):
        iCount = 1
        bFlag = False

        for i in Arr:
            if i == ch:
                bFlag = True
                break
            iCount += 1

        if bFlag == True:
            return iCount
        
        else:
            return -1
        

def main():

    Arr = input("Enter the string: ")
    cValue = input("Enter the charecter: ")[0]

    obj = Strings()
    iRet = obj.CheckPosition(Arr, cValue)

    if iRet == -1:
        print("Charecter not found")

    else:
        print("Position of charecter is: ",iRet)

if __name__ == "__main__":
    main()