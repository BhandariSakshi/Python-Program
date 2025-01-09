class Solution:

    def CheckBit(self, iNo):

        iMask = 136
        
        iResult = iNo & iMask

        if iResult == iMask:
            return True
        else:
            return False

def main():

    iValue = int(input("Enter the number: "))

    obj = Solution()

    bRet = obj.CheckBit(iValue)
    if bRet == True:
        print("4th and 8th bit is on")
    else:
        print("4th and 8th bit is off")

if __name__ == "__main__":
    main()